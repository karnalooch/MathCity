--[[
    Skrypt: AdminServer.luau
    Gdzie wkleić: ServerScriptService (jako zwykły Script)
    Opis: Obsługuje uprawnienia Admin Panelu (Gamepass za 500 Robux lub Twórca gry)
          oraz wykonuje polecenia: Fly, Noclip, GodMode, Speed, Dodawanie monet.
--]]

local MarketplaceService = game:GetService("MarketplaceService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local lastCommand = {}
local initialized = {}

-- TUTAJ WPISZ ID SWOJEGO GAMEPASSA ZA 500 ROBUX:
local ADMIN_GAMEPASS_ID = 0 -- Zmień na prawdziwe ID po stworzeniu Gamepassa w Roblox
local ADMIN_USER_IDS = {} -- Dla gry grupowej: np. {[12345678] = true}

-- Tworzymy folder na RemoteEvents w ReplicatedStorage
local remoteFolder = ReplicatedStorage:FindFirstChild("AdminRemotes")
if not remoteFolder then
    remoteFolder = Instance.new("Folder")
    remoteFolder.Name = "AdminRemotes"
    remoteFolder.Parent = ReplicatedStorage
end

local function getOrCreateRemote(name)
    local remote = remoteFolder:FindFirstChild(name)
    if not remote then
        remote = Instance.new("RemoteEvent")
        remote.Name = name
        remote.Parent = remoteFolder
    end
    return remote
end

local checkAdminEvent = getOrCreateRemote("CheckAdminStatus")
local commandEvent = getOrCreateRemote("ExecuteAdminCommand")

-- Sprawdzanie czy gracz ma prawo do Admina
local function isPlayerAdmin(player)
    -- 1. Twórca gry (Właściciel gry / Studio Test) zawsze ma darmowego Admina!
    if ADMIN_USER_IDS[player.UserId] == true
        or (game.CreatorType == Enum.CreatorType.User and player.UserId == game.CreatorId and game.CreatorId > 0)
        or (RunService:IsStudio() and game.CreatorId == 0) then
        return true
    end

    -- 2. Sprawdzenie czy gracz kupił Gamepass za 500 Robux
    if ADMIN_GAMEPASS_ID > 0 then
        local ownsPass = false
        pcall(function()
            ownsPass = MarketplaceService:UserOwnsGamePassAsync(player.UserId, ADMIN_GAMEPASS_ID)
        end)
        if ownsPass then
            return true
        end
    end

    return false
end

-- Po dołączeniu gracza informujemy klienta, czy ma Admina
local function revokeModes(player)
    local character = player.Character
    local humanoid = character and character:FindFirstChild("Humanoid")
    if humanoid then
        if player:GetAttribute("SpeedEnabled") == true then humanoid.WalkSpeed = 16 end
        if player:GetAttribute("GodMode") == true then
            humanoid.MaxHealth = 100
            humanoid.Health = math.min(humanoid.Health, 100)
        end
    end
    player:SetAttribute("GodMode", false)
    player:SetAttribute("SpeedEnabled", false)
end

local function refreshAdmin(player)
    local allowed = isPlayerAdmin(player)
    if player.Parent ~= Players then return end
    player:SetAttribute("IsAdmin", allowed)
    if not allowed then revokeModes(player) end
    checkAdminEvent:FireClient(player, allowed)
end

local function setupPlayer(player)
    if initialized[player] then return end
    initialized[player] = true
    player:SetAttribute("IsAdmin", false)
    local function resetModes()
        player:SetAttribute("GodMode", false)
        player:SetAttribute("SpeedEnabled", false)
    end
    resetModes()
    player.CharacterAdded:Connect(resetModes)
    task.spawn(refreshAdmin, player)
end
Players.PlayerAdded:Connect(setupPlayer)
for _, player in ipairs(Players:GetPlayers()) do setupPlayer(player) end
Players.PlayerRemoving:Connect(function(player)
    lastCommand[player], initialized[player] = nil, nil
end)
MarketplaceService.PromptGamePassPurchaseFinished:Connect(function(player, passId, purchased)
    if purchased and passId == ADMIN_GAMEPASS_ID then refreshAdmin(player) end
end)

-- Obsługa komend wysyłanych z Admin Panelu
commandEvent.OnServerEvent:Connect(function(player, command, value)
    if type(command) ~= "string" then return end
    local now = os.clock()
    if lastCommand[player] and now - lastCommand[player] < 0.2 then return end
    lastCommand[player] = now
    if not isPlayerAdmin(player) then
        player:SetAttribute("IsAdmin", false)
        revokeModes(player)
        warn(player.Name .. " próbował użyć Admin Panelu bez uprawnień!")
        return
    end
    if player.Parent ~= Players or player:GetAttribute("DataLoaded") ~= true then return end
    player:SetAttribute("IsAdmin", true)

    local character = player.Character
    if not character then return end
    local humanoid = character:FindFirstChild("Humanoid")

    if command == "SetSpeed" then
        if value ~= 16 and value ~= 60 then return end
        if humanoid then
            humanoid.WalkSpeed = value
            player:SetAttribute("SpeedEnabled", value == 60)
        end

    elseif command == "SetGodMode" then
        if type(value) ~= "boolean" then return end
        player:SetAttribute("GodMode", value == true)
        if humanoid and value == true then
            humanoid.MaxHealth = math.huge
            humanoid.Health = math.huge
        elseif humanoid and value == false then
            humanoid.MaxHealth = 100
            humanoid.Health = 100
        end

    elseif command == "AddCoins" then
        local leaderstats = player:FindFirstChild("leaderstats")
        if leaderstats and leaderstats:FindFirstChild("Coins") then
            leaderstats.Coins.Value = math.min(1000000000, leaderstats.Coins.Value + 500)
        end

    elseif command == "AddGems" then
        local leaderstats = player:FindFirstChild("leaderstats")
        if leaderstats and leaderstats:FindFirstChild("Gems") then
            leaderstats.Gems.Value = math.min(1000000000, leaderstats.Gems.Value + 100)
        end
    end
end)
