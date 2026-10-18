-- Script w ServerScriptService. Zachowuje dotychczasowy magazyn i klucze danych.
local DataStoreService = game:GetService("DataStoreService")
local Players = game:GetService("Players")
local HttpService = game:GetService("HttpService")
local RunService = game:GetService("RunService")
local localPreview = RunService:IsStudio() and game.GameId == 0
local store
if localPreview then
    -- Nieopublikowana mapa: dane tylko na czas testu, bez dostępu do kont graczy.
    local memory = {}
    store = {UpdateAsync = function(_, key, transform)
        local result = transform(memory[key])
        if result ~= nil then memory[key] = result end
        return result
    end}
    warn("TRYB LOKALNY: postęp nie jest zachowywany po zatrzymaniu Play.")
else
    store = DataStoreService:GetDataStore("MathTowerData_v1")
end
local AUTOSAVE_SECONDS = 60
local SESSION_SECONDS = 180
local MAX_VALUE = 1000000000
local sessions = {}
local closing = false

local function validNumber(value, minimum)
    return type(value) == "number" and value == value and value >= minimum
        and value <= MAX_VALUE and value % 1 == 0
end

local function validData(data)
    return type(data) == "table" and validNumber(data.Stage, 1)
        and validNumber(data.Coins, 0) and validNumber(data.Gems or 0, 0)
end

local function retry(callback)
    local lastError
    for attempt = 1, 3 do
        local ok, result = pcall(callback)
        if ok then return true, result end
        lastError = result
        if attempt < 3 then task.wait(attempt) end
    end
    warn("DataStore: " .. tostring(lastError))
    return false, nil
end

local function save(player, release)
    local session = sessions[player]
    if not session then return end
    if release then session.leaving = true end
    while session.busy do task.wait(0.05) end
    if not session.loaded or session.released then return end
    session.busy = true
    local stats = player:FindFirstChild("leaderstats")
    local data = stats and {Stage = stats.Stage.Value, Coins = stats.Coins.Value, Gems = stats.Gems.Value}
    if not validData(data) then
        session.busy = false
        warn("Odmowa zapisu nieprawidłowych danych: " .. player.Name)
        return
    end
    local ok, saved = retry(function()
        return store:UpdateAsync("Player_" .. player.UserId, function(old)
            if type(old) ~= "table" or type(old.Session) ~= "table" or old.Session.Id ~= session.id then
                return nil
            end
            local result = table.clone(old)
            result.Stage, result.Coins, result.Gems = data.Stage, data.Coins, data.Gems
            result.Session = not release and {Id = session.id, ExpiresAt = os.time() + SESSION_SECONDS} or nil
            return result
        end)
    end)
    session.busy = false
    if ok and saved then
        if release then
            session.released = true
            sessions[player] = nil
        end
    elseif ok then
        session.loaded = false
        player:SetAttribute("DataLoaded", false)
        player:Kick("Sesja danych wygasła. Dołącz ponownie.")
    else
        warn("Nie udało się zapisać danych: " .. player.Name)
    end
end

local function onPlayerAdded(player)
    if sessions[player] or closing then return end
    local session = {id = HttpService:GenerateGUID(false), busy = true, loaded = false}
    sessions[player] = session
    player:SetAttribute("DataLoaded", false)
    local ok, data = retry(function()
        return store:UpdateAsync("Player_" .. player.UserId, function(old)
            if old == nil then old = {Stage = 1, Coins = 0, Gems = 0} end
            if not validData(old) then return nil end
            local lock = old.Session
            if lock ~= nil then
                if type(lock) ~= "table" or type(lock.ExpiresAt) ~= "number" then return nil end
                if lock.Id ~= session.id and lock.ExpiresAt > os.time() then return nil end
            end
            local result = table.clone(old)
            result.Gems = result.Gems or 0
            result.Session = {Id = session.id, ExpiresAt = os.time() + SESSION_SECONDS}
            return result
        end)
    end)
    if not ok or not data then
        session.busy = false
        sessions[player] = nil
        player:Kick("Nie można bezpiecznie wczytać danych. Spróbuj ponownie za chwilę.")
        return
    end

    local stats = Instance.new("Folder")
    stats.Name = "leaderstats"
    for _, name in ipairs({"Stage", "Coins", "Gems"}) do
        local stat = Instance.new("IntValue")
        stat.Name, stat.Value, stat.Parent = name, data[name], stats
    end
    stats.Parent = player
    session.loaded, session.busy = true, false
    if session.leaving or player.Parent ~= Players or closing then
        save(player, true)
        return
    end
    player:SetAttribute("DataLoaded", true)

    local function moveToCheckpoint(character)
        local root = character:WaitForChild("HumanoidRootPart", 5)
        if not root or player.Character ~= character then return end
        local folder = workspace:FindFirstChild("Checkpoints")
        local checkpoint = folder and folder:FindFirstChild(tostring(stats.Stage.Value))
        if checkpoint and checkpoint:IsA("BasePart") then
            root.CFrame = checkpoint.CFrame + Vector3.new(0, 3.5, 0)
        end
    end
    player.CharacterAdded:Connect(moveToCheckpoint)
    if player.Character then task.spawn(moveToCheckpoint, player.Character) end
end

Players.PlayerAdded:Connect(onPlayerAdded)
Players.PlayerRemoving:Connect(function(player)
    player:SetAttribute("DataLoaded", false)
    save(player, true)
end)
for _, player in ipairs(Players:GetPlayers()) do task.spawn(onPlayerAdded, player) end

task.spawn(function()
    while not closing do
        task.wait(AUTOSAVE_SECONDS)
        if closing then break end
        for player, session in pairs(sessions) do
            if session.loaded and not session.leaving then task.spawn(save, player, false) end
        end
    end
end)

game:BindToClose(function()
    closing = true
    local pending = 0
    for player in pairs(sessions) do
        pending += 1
        task.spawn(function()
            save(player, true)
            pending -= 1
        end)
    end
    local deadline = os.clock() + 25
    while pending > 0 and os.clock() < deadline do task.wait(0.05) end
    if pending > 0 then warn("Nie wszystkie zapisy zakończyły się przed zamknięciem serwera.") end
end)
