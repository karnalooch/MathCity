--[[
    Skrypt: AdminPanelGui.luau
    Gdzie wkleić: StarterPlayer -> StarterPlayerScripts LUB StarterGui -> LocalScript
    Opis: Tworzy piękny panel administracyjny na ekranie z przyciskami do Latania (Fly),
          Przechodzenia przez ściany (Noclip), Super Szybkości, Nieśmiertelności i Monet.
--]]

local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local ContextActionService = game:GetService("ContextActionService")

local player = Players.LocalPlayer

-- Folder RemoteEvents
local adminRemotes = ReplicatedStorage:WaitForChild("AdminRemotes", 10)
local commandEvent = adminRemotes and adminRemotes:WaitForChild("ExecuteAdminCommand", 10)

-- Stany funkcji
local isFlying = false
local isNoclip = false
local isSpeed = false
local isGodMode = false
local buttons = {}
local originalCollisions = {}
local flyUp, flyDown = false, false

local function canUseAdmin()
    return player:GetAttribute("IsAdmin") == true and player:GetAttribute("DataLoaded") == true
end

-- Tworzenie UI
local playerGui = player:WaitForChild("PlayerGui")
local screenGui = Instance.new("ScreenGui")
screenGui.Name = "AdminGui"
screenGui.ResetOnSpawn = false
screenGui.Enabled = false
screenGui.Parent = playerGui

-- Przycisk otwierania panelu
local openBtn = Instance.new("TextButton")
openBtn.Size = UDim2.new(0, 110, 0, 40)
openBtn.Position = UDim2.new(0, 15, 0.5, -20)
openBtn.BackgroundColor3 = Color3.fromRGB(240, 170, 0)
openBtn.Text = "👑 ADMIN"
openBtn.Font = Enum.Font.FredokaOne
openBtn.TextColor3 = Color3.fromRGB(255, 255, 255)
openBtn.TextSize = 18
openBtn.Parent = screenGui

local corner = Instance.new("UICorner")
corner.CornerRadius = UDim.new(0, 8)
corner.Parent = openBtn

-- Główne okno panelu
local frame = Instance.new("Frame")
frame.Size = UDim2.new(0, 260, 0, 360)
frame.Position = UDim2.new(0.5, -130, 0.5, -180)
frame.BackgroundColor3 = Color3.fromRGB(30, 30, 40)
frame.BorderSizePixel = 0
frame.Visible = false
frame.Parent = screenGui

local frameCorner = Instance.new("UICorner")
frameCorner.CornerRadius = UDim.new(0, 12)
frameCorner.Parent = frame

local title = Instance.new("TextLabel")
title.Size = UDim2.new(1, 0, 0, 45)
title.BackgroundTransparency = 1
title.Text = "MATH CITY · ADMIN"
title.Font = Enum.Font.FredokaOne
title.TextColor3 = Color3.fromRGB(255, 215, 0)
title.TextSize = 20
title.Parent = frame

local listLayout = Instance.new("UIListLayout")
listLayout.Padding = UDim.new(0, 8)
listLayout.HorizontalAlignment = Enum.HorizontalAlignment.Center
listLayout.SortOrder = Enum.SortOrder.LayoutOrder
listLayout.Parent = frame

title.LayoutOrder = 0

openBtn.Activated:Connect(function()
    if not canUseAdmin() then return end
    frame.Visible = not frame.Visible
end)

-- Funkcja pomocnicza do tworzenia przycisków w menu
local function createMenuButton(text, order, callback)
    local btn = Instance.new("TextButton")
    btn.Size = UDim2.new(0, 220, 0, 40)
    btn.BackgroundColor3 = Color3.fromRGB(50, 50, 65)
    btn.Text = text
    btn.Font = Enum.Font.FredokaOne
    btn.TextColor3 = Color3.fromRGB(255, 255, 255)
    btn.TextSize = 16
    btn.LayoutOrder = order
    btn.Parent = frame

    local btnCorner = Instance.new("UICorner")
    btnCorner.CornerRadius = UDim.new(0, 8)
    btnCorner.Parent = btn

    buttons[order] = btn
    btn.Activated:Connect(function()
        if not canUseAdmin() then return end
        callback(btn)
    end)
    return btn
end

-- ================= 1. FLY (LATANIE) =================
local flySpeed = 50
local bodyVelocity, bodyGyro

local function startFlying()
    if not canUseAdmin() then return false end
    local char = player.Character
    if not char then return false end
    local root = char:FindFirstChild("HumanoidRootPart")
    if not root then return false end

    bodyVelocity = Instance.new("BodyVelocity")
    bodyVelocity.Velocity = Vector3.zero
    bodyVelocity.MaxForce = Vector3.new(1e5, 1e5, 1e5)
    bodyVelocity.Parent = root

    bodyGyro = Instance.new("BodyGyro")
    bodyGyro.MaxTorque = Vector3.new(1e5, 1e5, 1e5)
    bodyGyro.CFrame = root.CFrame
    bodyGyro.Parent = root
    ContextActionService:BindAction("AdminFlyUp", function(_, state)
        flyUp = state == Enum.UserInputState.Begin
        return Enum.ContextActionResult.Sink
    end, true, Enum.KeyCode.Space, Enum.KeyCode.ButtonA)
    ContextActionService:BindAction("AdminFlyDown", function(_, state)
        flyDown = state == Enum.UserInputState.Begin
        return Enum.ContextActionResult.Sink
    end, true, Enum.KeyCode.LeftShift, Enum.KeyCode.ButtonB)
    ContextActionService:SetTitle("AdminFlyUp", "↑")
    ContextActionService:SetTitle("AdminFlyDown", "↓")
    ContextActionService:SetPosition("AdminFlyUp", UDim2.new(1, -150, 1, -180))
    ContextActionService:SetPosition("AdminFlyDown", UDim2.new(1, -80, 1, -180))
    return true
end

local function stopFlying()
    if bodyVelocity then bodyVelocity:Destroy() bodyVelocity = nil end
    if bodyGyro then bodyGyro:Destroy() bodyGyro = nil end
    ContextActionService:UnbindAction("AdminFlyUp")
    ContextActionService:UnbindAction("AdminFlyDown")
    flyUp, flyDown = false, false
end

RunService.RenderStepped:Connect(function()
    if canUseAdmin() and isFlying and bodyVelocity and bodyGyro and player.Character then
        local cam = workspace.CurrentCamera
        local root = player.Character:FindFirstChild("HumanoidRootPart")
        if not root or not cam then return end
        if UserInputService:GetFocusedTextBox() then
            bodyVelocity.Velocity = Vector3.zero
            return
        end

        local moveDir = Vector3.zero
        if UserInputService:IsKeyDown(Enum.KeyCode.W) then moveDir = moveDir + cam.CFrame.LookVector end
        if UserInputService:IsKeyDown(Enum.KeyCode.S) then moveDir = moveDir - cam.CFrame.LookVector end
        if UserInputService:IsKeyDown(Enum.KeyCode.A) then moveDir = moveDir - cam.CFrame.RightVector end
        if UserInputService:IsKeyDown(Enum.KeyCode.D) then moveDir = moveDir + cam.CFrame.RightVector end
        local humanoid = player.Character:FindFirstChild("Humanoid")
        if moveDir.Magnitude == 0 and humanoid then moveDir = humanoid.MoveDirection end
        if flyUp then moveDir = moveDir + Vector3.new(0, 1, 0) end
        if flyDown then moveDir = moveDir - Vector3.new(0, 1, 0) end
        if moveDir.Magnitude > 1 then moveDir = moveDir.Unit end

        bodyVelocity.Velocity = moveDir * flySpeed
        bodyGyro.CFrame = cam.CFrame
    end
end)

createMenuButton("🪽 Fly: OFF", 1, function(btn)
    if isFlying then stopFlying() isFlying = false else isFlying = startFlying() end
    btn.Text = isFlying and "🪽 Fly: ON (WASD+Spacja)" or "🪽 Fly: OFF"
    btn.BackgroundColor3 = isFlying and Color3.fromRGB(46, 204, 113) or Color3.fromRGB(50, 50, 65)
end)

-- ================= 2. NOCLIP (PRZECHODZENIE PRZEZ ŚCIANY) =================
RunService.Stepped:Connect(function()
    if canUseAdmin() and isNoclip and player.Character then
        for _, part in ipairs(player.Character:GetDescendants()) do
            if part:IsA("BasePart") then
                if originalCollisions[part] == nil then originalCollisions[part] = part.CanCollide end
                part.CanCollide = false
            end
        end
    end
end)

local function restoreCollisions()
    for part, value in pairs(originalCollisions) do
        if part.Parent then part.CanCollide = value end
    end
    table.clear(originalCollisions)
end

createMenuButton("👻 Noclip: OFF", 2, function(btn)
    isNoclip = not isNoclip
    if not isNoclip then restoreCollisions() end
    btn.Text = isNoclip and "👻 Noclip: ON" or "👻 Noclip: OFF"
    btn.BackgroundColor3 = isNoclip and Color3.fromRGB(46, 204, 113) or Color3.fromRGB(50, 50, 65)
end)

-- ================= 3. SUPER SPEED =================
createMenuButton("⚡ Speed: OFF", 3, function(btn)
    if commandEvent then
        commandEvent:FireServer("SetSpeed", isSpeed and 16 or 60)
    end
end)

-- ================= 4. GOD MODE =================
createMenuButton("🛡️ God Mode: OFF", 4, function(btn)
    if commandEvent then
        commandEvent:FireServer("SetGodMode", not isGodMode)
    end
end)

-- ================= 5. DODAJ 500 MONET =================
createMenuButton("💰 +500 Monet ($)", 5, function()
    if commandEvent then
        commandEvent:FireServer("AddCoins", 500)
    end
end)

-- ================= 6. DODAJ 100 KRYSZTAŁÓW =================
createMenuButton("💎 +100 Kryształów", 6, function()
    if commandEvent then
        commandEvent:FireServer("AddGems", 100)
    end
end)

local function resetLocalModes()
    stopFlying()
    restoreCollisions()
    isFlying, isNoclip = false, false
    for index, label in ipairs({"🪽 Fly: OFF", "👻 Noclip: OFF"}) do
        buttons[index].Text = label
        buttons[index].BackgroundColor3 = Color3.fromRGB(50, 50, 65)
    end
end

local function syncServerModes()
    isSpeed = player:GetAttribute("SpeedEnabled") == true
    isGodMode = player:GetAttribute("GodMode") == true
    buttons[3].Text = isSpeed and "⚡ Speed: 60" or "⚡ Speed: OFF"
    buttons[4].Text = isGodMode and "🛡️ God Mode: ON" or "🛡️ God Mode: OFF"
    buttons[3].BackgroundColor3 = isSpeed and Color3.fromRGB(46, 204, 113) or Color3.fromRGB(50, 50, 65)
    buttons[4].BackgroundColor3 = isGodMode and Color3.fromRGB(46, 204, 113) or Color3.fromRGB(50, 50, 65)
end

local function syncAccess()
    screenGui.Enabled = canUseAdmin()
    if not screenGui.Enabled then
        frame.Visible = false
        resetLocalModes()
    end
end
player:GetAttributeChangedSignal("IsAdmin"):Connect(syncAccess)
player:GetAttributeChangedSignal("DataLoaded"):Connect(syncAccess)
player:GetAttributeChangedSignal("SpeedEnabled"):Connect(syncServerModes)
player:GetAttributeChangedSignal("GodMode"):Connect(syncServerModes)
player.CharacterRemoving:Connect(resetLocalModes)
player.CharacterAdded:Connect(function()
    resetLocalModes()
    syncServerModes()
end)
syncAccess()
syncServerModes()
