-- Service doubles: these checks do not simulate physics or live persistence.
local function signal()
    local callbacks = {}
    return {
        Connect = function(_, fn) table.insert(callbacks, fn) end,
        Fire = function(_, ...)
            for _, fn in ipairs(callbacks) do fn(...) end
        end,
    }
end

local function object(class)
    local obj = {ClassName = class, children = {}, attributes = {}, signals = {}}
    obj.Activated = signal()
    obj.Touched = signal()
    obj.OnServerEvent = signal()
    obj.CharacterAdded, obj.CharacterRemoving = signal(), signal()
    function obj:FindFirstChild(name) return self.children[name] end
    obj.WaitForChild = obj.FindFirstChild
    function obj:GetAttribute(name) return self.attributes[name] end
    function obj:GetAttributeChangedSignal(name)
        if not self.signals[name] then self.signals[name] = signal() end
        return self.signals[name]
    end
    function obj:SetAttribute(name, value)
        local changed = self.attributes[name] ~= value
        self.attributes[name] = value
        if changed then self:GetAttributeChangedSignal(name):Fire() end
    end
    function obj:FireClient() end
    function obj:FireServer(...) self.sent = {...} end
    function obj:Kick(reason) self.kicked = reason end
    function obj:IsA(name) return self.ClassName == name end
    function obj:GetDescendants()
        local result = {}
        for _, child in pairs(self.children) do table.insert(result, child) end
        return result
    end
    function obj:Destroy() self.destroyed = true end
    return setmetatable(obj, {
        __index = function(t, key) return t.children[key] end,
        __newindex = function(t, key, value)
            if key == "Parent" and value then value.children[t.Name or class] = t end
            rawset(t, key, value)
        end,
    })
end

local function setup(options)
    options = options or {}
    local queue = {}
    local created = {}
    local players = object("Players")
    players.PlayerAdded, players.PlayerRemoving = signal(), signal()
    local player = object("Player")
    player.Name, player.UserId, player.Parent = "Tester", options.userId or 42, players
    players.LocalPlayer = player
    function players:GetPlayers() return {player} end
    local character = object("Model")
    local humanoid = object("Humanoid")
    humanoid.Name, humanoid.WalkSpeed, humanoid.Health, humanoid.Parent = "Humanoid", 16, 100, character
    local root = object("BasePart")
    root.Name, root.Parent, root.CFrame, root.CanCollide = "HumanoidRootPart", character, 0, true
    local other = object("BasePart")
    other.Name, other.Parent, other.CanCollide = "Other", character, false
    player.Character = character
    function players:GetPlayerFromCharacter(value) return value == character and player or nil end
    local gui = object("PlayerGui")
    gui.Name, gui.Parent = "PlayerGui", player
    local run = {RenderStepped = signal(), Stepped = signal()}
    function run:IsStudio() return options.studio == true end
    local market = {PromptGamePassPurchaseFinished = signal()}
    function market:UserOwnsGamePassAsync()
        if options.passError then error("lookup failed") end
        return options.pass == true
    end
    local store = {value = options.saved, writes = 0, calls = 0}
    function store:UpdateAsync(_, callback)
        self.calls += 1
        if options.failStore then error("network error") end
        if options.failOnce then options.failOnce = false error("temporary error") end
        local value = callback(self.value)
        if value ~= nil then self.value = value self.writes += 1 end
        return value
    end
    local services = {
        Players = players, RunService = run, MarketplaceService = market,
        ReplicatedStorage = object("ReplicatedStorage"),
        DataStoreService = {GetDataStore = function() return store end},
        HttpService = {GenerateGUID = function() return "session-test" end},
        UserInputService = {IsKeyDown = function() return false end, GetFocusedTextBox = function() return nil end},
        ContextActionService = {BindAction = function() end, UnbindAction = function() end,
            SetTitle = function() end, SetPosition = function() end},
    }
    local game = {CreatorId = options.creatorId or 42, CreatorType = options.creatorType or "User", GameId = options.gameId or 123}
    function game:GetService(name) assert(services[name], name) return services[name] end
    game.Players = players
    function game:BindToClose(fn) self.close = fn end
    local clockValue = 100
    local env = setmetatable({
        game = game, workspace = object("Workspace"), Instance = {new = function(class)
            local value = object(class)
            table.insert(created, value)
            return value
        end},
        Enum = {CreatorType = {User = "User"}, Font = {FredokaOne = 1},
            HorizontalAlignment = {Center = 1}, SortOrder = {LayoutOrder = 1},
            KeyCode = {}, UserInputState = {Begin = 1}, ContextActionResult = {Sink = 1},
            Material = {Neon = 1, SmoothPlastic = 2}, NormalId = {Front = 1}},
        UDim2 = {new = function() return 0 end}, UDim = {new = function() return 0 end},
        Color3 = {fromRGB = function(r, g, b) return tostring(r)..","..g..","..b end},
        Vector3 = {zero = 0, new = function() return 3.5 end},
        warn = function() end,
        os = {time = os.time, clock = function() clockValue += 1 return clockValue end},
        task = {
            wait = function() end,
            spawn = function(fn, ...) table.insert(queue, {fn, {...}}) end,
            delay = function(_, fn) table.insert(queue, {fn, {}}) end,
        },
    }, {__index = getfenv()})
    local function execute(name, transform)
        local source = SOURCES[name]
        if transform then source = transform(source) end
        local fn = assert(loadstring(source, name))
        setfenv(fn, env)()
    end
    local function nextTask()
        local entry = table.remove(queue, 1)
        assert(entry, "no queued task")
        entry[1](unpack(entry[2]))
    end
    local function startTask()
        local entry = table.remove(queue, 1)
        local thread = coroutine.create(entry[1])
        assert(coroutine.resume(thread, unpack(entry[2])))
        return thread
    end
    return {env = env, player = player, players = players, services = services, store = store,
        execute = execute, nextTask = nextTask, startTask = startTask, root = root, other = other,
        options = options, created = created}
end

local cases = 0
local function test(name, fn)
    fn()
    cases += 1
    print("PASS " .. name)
end

for _, case in ipairs({
    {name = "owner", allowed = true},
    {name = "ordinary user", userId = 99, allowed = false},
    {name = "group ID collision", creatorType = "Group", allowed = false},
    {name = "unpublished Studio", creatorId = 0, studio = true, allowed = true},
    {name = "zero ID live", creatorId = 0, allowed = false},
    {name = "pass owner", userId = 99, pass = true, allowed = true},
    {name = "pass lookup failure", userId = 99, passError = true, allowed = false},
}) do
    test("authorization: " .. case.name, function()
        local c = setup(case)
        c.execute("AdminServer", function(s) return (s:gsub("local ADMIN_GAMEPASS_ID = 0", "local ADMIN_GAMEPASS_ID = 123")) end)
        c.nextTask()
        assert(c.player:GetAttribute("IsAdmin") == case.allowed)
        c.player:SetAttribute("DataLoaded", true)
        local remote = c.services.ReplicatedStorage.AdminRemotes.ExecuteAdminCommand
        remote.OnServerEvent:Fire(c.player, "SetSpeed", 60)
        assert(c.player.Character.Humanoid.WalkSpeed == (case.allowed and 60 or 16))
        remote.OnServerEvent:Fire(c.player, "SetSpeed", math.huge)
        assert(c.player.Character.Humanoid.WalkSpeed == (case.allowed and 60 or 16))
        remote.OnServerEvent:Fire(c.player, "SetGodMode", "true")
        assert(c.player:GetAttribute("GodMode") == false)
    end)
end

test("failed load never saves defaults", function()
    local c = setup({failStore = true, saved = {Stage = 8, Coins = 300, Gems = 4}})
    c.execute("LeaderstatsAndDataStore") c.nextTask()
    assert(c.store.calls == 3 and c.store.writes == 0 and c.player.kicked)
    c.players.PlayerRemoving:Fire(c.player)
    assert(c.store.writes == 0 and c.store.value.Stage == 8)
end)

test("unpublished Studio uses session-only data", function()
    local c = setup({studio = true, gameId = 0, failStore = true})
    c.execute("LeaderstatsAndDataStore") c.nextTask()
    assert(c.player:GetAttribute("DataLoaded") == true and c.store.calls == 0)
    assert(c.player.leaderstats.Stage.Value == 1)
    c.players.PlayerRemoving:Fire(c.player)
    assert(c.store.calls == 0)
end)

test("published Studio never falls back after store failure", function()
    local c = setup({studio = true, gameId = 123, failStore = true})
    c.execute("LeaderstatsAndDataStore") c.nextTask()
    assert(c.player.kicked and c.player:GetAttribute("DataLoaded") == false and c.store.calls == 3)
end)

test("existing character checkpoint, retry and successful release", function()
    local c = setup({failOnce = true, saved = {Stage = 8, Coins = 300}})
    local folder = object("Folder") folder.Name, folder.Parent = "Checkpoints", c.env.workspace
    local checkpoint = object("BasePart") checkpoint.Name, checkpoint.CFrame, checkpoint.Parent = "8", 100, folder
    c.execute("LeaderstatsAndDataStore") c.nextTask()
    assert(c.player:GetAttribute("DataLoaded") and c.player.leaderstats.Gems.Value == 0)
    -- First queued function is the autosave loop; skip it in the synchronous double.
    -- The checkpoint task is tested by firing the same callback on the existing character.
    c.player.CharacterAdded:Fire(c.player.Character)
    assert(c.root.CFrame == 103.5)
    c.player.leaderstats.Coins.Value = 350
    c.players.PlayerRemoving:Fire(c.player)
    assert(c.store.value.Coins == 350 and c.store.value.Session == nil)
end)

test("active foreign session cannot be overwritten", function()
    local c = setup({saved = {Stage = 8, Coins = 300, Gems = 4, Session = {Id = "other", ExpiresAt = os.time() + 500}}})
    c.execute("LeaderstatsAndDataStore") c.nextTask()
    assert(c.player.kicked and c.store.writes == 0)
end)

test("session takeover blocks stale save", function()
    local c = setup()
    c.execute("LeaderstatsAndDataStore") c.nextTask()
    c.store.value.Session.Id = "new-server"
    c.store.value.Coins = 999
    c.players.PlayerRemoving:Fire(c.player)
    assert(c.store.value.Coins == 999 and c.player:GetAttribute("DataLoaded") == false)
end)

test("server currency amounts and respawn state", function()
    local c = setup()
    c.execute("LeaderstatsAndDataStore") c.nextTask()
    c.execute("AdminServer")
    local remote = c.services.ReplicatedStorage.AdminRemotes.ExecuteAdminCommand
    remote.OnServerEvent:Fire(c.player, "AddCoins", math.huge)
    remote.OnServerEvent:Fire(c.player, "AddGems", -500)
    assert(c.player.leaderstats.Coins.Value == 500 and c.player.leaderstats.Gems.Value == 100)
    remote.OnServerEvent:Fire(c.player, "SetSpeed", 60)
    remote.OnServerEvent:Fire(c.player, "SetGodMode", true)
    assert(c.player:GetAttribute("SpeedEnabled") and c.player:GetAttribute("GodMode"))
    c.player.CharacterAdded:Fire(c.player.Character)
    assert(not c.player:GetAttribute("SpeedEnabled") and not c.player:GetAttribute("GodMode"))
end)

test("autosave retries and shutdown saves then releases", function()
    local c = setup()
    c.execute("LeaderstatsAndDataStore") c.nextTask()
    c.env.task.wait = coroutine.yield
    local autosave = c.startTask() -- Suspended at the 60-second interval.
    c.nextTask() -- Initial character checkpoint.
    c.player.leaderstats.Coins.Value = 700
    assert(coroutine.resume(autosave)) -- Enqueues one autosave.
    c.options.failOnce = true
    local saving = c.startTask() -- First request fails, retry waits.
    assert(coroutine.resume(saving))
    assert(c.store.value.Coins == 700 and c.store.value.Session ~= nil)
    c.player.leaderstats.Coins.Value = 800
    local closing = coroutine.create(c.env.game.close)
    assert(coroutine.resume(closing)) -- Enqueues final save and waits.
    c.nextTask()
    assert(coroutine.resume(closing))
    assert(c.store.value.Coins == 800 and c.store.value.Session == nil)
end)

test("door restores color and ignores old close timer", function()
    local c = setup()
    local floor = object("Model")
    for _, name in ipairs({"Door1", "Door2", "Door3", "Sign"}) do
        local part = object("BasePart")
        part.Name, part.Color, part.Transparency, part.Parent = name, "blue", 0.2, floor
    end
    c.env.script = {Parent = floor}
    c.execute("MathDoorScript")
    floor.Door2.Touched:Fire(c.root)
    assert(floor.Door2.CanCollide == true) -- Data not loaded.
    c.player:SetAttribute("DataLoaded", true)
    floor.Door2.Touched:Fire(c.root)
    floor.Door2.Touched:Fire(c.root)
    c.nextTask()
    assert(floor.Door2.CanCollide == false)
    c.nextTask()
    assert(floor.Door2.CanCollide == true and floor.Door2.Color == "blue" and floor.Door2.Transparency == 0.2)
end)

test("client reads entitlement published before startup", function()
    local c = setup()
    c.execute("AdminServer") c.nextTask()
    c.player:SetAttribute("DataLoaded", true)
    c.execute("AdminPanelGui")
    assert(c.player.PlayerGui.AdminGui.Enabled)
end)

test("revoked entitlement clears live server effects", function()
    local c = setup({userId = 99, pass = true})
    c.execute("AdminServer", function(s) return (s:gsub("local ADMIN_GAMEPASS_ID = 0", "local ADMIN_GAMEPASS_ID = 123")) end)
    c.nextTask()
    c.player:SetAttribute("DataLoaded", true)
    local remote = c.services.ReplicatedStorage.AdminRemotes.ExecuteAdminCommand
    remote.OnServerEvent:Fire(c.player, "SetSpeed", 60)
    remote.OnServerEvent:Fire(c.player, "SetGodMode", true)
    c.options.pass = false
    remote.OnServerEvent:Fire(c.player, "SetSpeed", 60)
    assert(not c.player:GetAttribute("IsAdmin"))
    assert(not c.player:GetAttribute("GodMode") and not c.player:GetAttribute("SpeedEnabled"))
    assert(c.player.Character.Humanoid.WalkSpeed == 16 and c.player.Character.Humanoid.MaxHealth == 100)
end)

test("client entitlement, revoke, noclip restore and respawn", function()
    local c = setup({userId = 99})
    c.execute("AdminServer") c.nextTask()
    c.execute("AdminPanelGui")
    local gui = c.player.PlayerGui.AdminGui
    local frame = gui.Frame
    local buttons = {}
    for _, value in ipairs(c.created) do
        if value.ClassName == "TextButton" and value.LayoutOrder then buttons[value.LayoutOrder] = value end
    end
    assert(gui.Enabled == false)
    buttons[1].Activated:Fire()
    buttons[2].Activated:Fire()
    c.services.RunService.Stepped:Fire()
    assert(not c.root.BodyVelocity and c.root.CanCollide == true)
    gui.TextButton.Activated:Fire()
    assert(frame.Visible == false)
    c.player:SetAttribute("DataLoaded", true)
    c.player:SetAttribute("IsAdmin", true)
    assert(gui.Enabled == true)
    gui.TextButton.Activated:Fire()
    assert(frame.Visible == true)
    buttons[1].Activated:Fire()
    buttons[2].Activated:Fire()
    c.services.RunService.Stepped:Fire()
    assert(c.root.BodyVelocity and c.root.CanCollide == false)
    local mover = c.root.BodyVelocity
    c.player:SetAttribute("IsAdmin", false)
    assert(gui.Enabled == false and frame.Visible == false)
    assert(mover.destroyed and c.root.CanCollide == true and c.other.CanCollide == false)
    c.player:SetAttribute("IsAdmin", true)
    buttons[2].Activated:Fire()
    c.services.RunService.Stepped:Fire()
    c.player.CharacterRemoving:Fire(c.player.Character)
    assert(c.root.CanCollide == true and c.other.CanCollide == false)
end)

print("Passed " .. cases .. " regression scenarios")
