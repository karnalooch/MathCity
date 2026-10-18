assert(not game:GetService("RunService"):IsRunning(), "Zatrzymaj Play przed importem")
assert(not workspace:FindFirstChild("MathCity") and not workspace:FindFirstChild("MathAdventure"), "Mapa jest już dodana; nie importuj jej ponownie")
local SSS = game:GetService("ServerScriptService")
local starter = game:GetService("StarterPlayer").StarterPlayerScripts
local function addScript(parent, name, class, source)
    assert(not parent:FindFirstChild(name), "Skrypt już istnieje: " .. name)
    local value = Instance.new(class)
    value.Name, value.Source, value.Parent = name, source, parent
    return value
end
local map = Instance.new("Model")
map.Name, map.Parent = "MathCity", workspace
local function part(parent, name, size, position, color)
    local value = Instance.new("Part")
    value.Name, value.Size, value.Position = name, size, position
    value.Anchored = true
    value.Color = color or Color3.fromRGB(35, 43, 68)
    value.Material = Enum.Material.SmoothPlastic
    value.TopSurface, value.BottomSurface = Enum.SurfaceType.Smooth, Enum.SurfaceType.Smooth
    value.Parent = parent
    return value
end
local function label(value, text, color)
    local gui = Instance.new("SurfaceGui")
    gui.Face, gui.CanvasSize, gui.Parent = Enum.NormalId.Front, Vector2.new(value.Size.X * 40, value.Size.Y * 40), value
    local textLabel = Instance.new("TextLabel")
    textLabel.Name = "TextLabel"
    textLabel.Size, textLabel.BackgroundTransparency = UDim2.fromScale(1, 1), 1
    textLabel.Text, textLabel.TextScaled = text, true
    textLabel.Font, textLabel.TextColor3 = Enum.Font.FredokaOne, color or Color3.new(1, 1, 1)
    textLabel.Parent = gui
end
local cyan, purple = Color3.fromRGB(30, 210, 235), Color3.fromRGB(162, 94, 255)
part(map, "CourseFloor", Vector3.new(44, 2, 150), Vector3.new(0, 1, -51))
part(map, "LeftWall", Vector3.new(2, 25, 150), Vector3.new(-23, 14, -51))
part(map, "RightWall", Vector3.new(2, 25, 150), Vector3.new(23, 14, -51))
part(map, "BackWall", Vector3.new(48, 25, 2), Vector3.new(0, 14, 24))
part(map, "FinishWall", Vector3.new(48, 25, 2), Vector3.new(0, 14, -126))
for _, x in ipairs({-21, 21}) do
    local strip = part(map, "LightStrip", Vector3.new(0.4, 0.1, 146), Vector3.new(x, 2.1, -51), cyan)
    strip.Material = Enum.Material.Neon
end
local checkpoints = Instance.new("Folder")
checkpoints.Name, checkpoints.Parent = "Checkpoints", workspace
for i, z in ipairs({10, -32, -68, -106}) do
    local cp = part(checkpoints, tostring(i), Vector3.new(8, 0.25, 5), Vector3.new(0, 2.2, z), cyan)
    cp.Material, cp.CanCollide = Enum.Material.Neon, false
end
local spawn = workspace:FindFirstChildWhichIsA("SpawnLocation", true)
if not spawn then spawn = Instance.new("SpawnLocation") spawn.Parent = map end
spawn.Anchored, spawn.Neutral, spawn.Duration = true, true, 0
spawn.Size, spawn.CFrame = Vector3.new(8, 0.3, 5), CFrame.new(0, 2.3, 10)
spawn.Transparency, spawn.CanCollide = 1, false
local questions = {
    {"7 x 8 = ?", {"48", "56", "64"}, 2},
    {"81 / 9 = ?", {"9", "8", "7"}, 1},
    {"15 + 27 = ?", {"32", "41", "42"}, 3},
}
for i, question in ipairs(questions) do
    local z = -22 - (i - 1) * 36
    local floor = Instance.new("Model")
    floor.Name, floor.Parent = "Floor" .. i, map
    for doorIndex, x in ipairs({-14, 0, 14}) do
        local door = part(floor, "Door" .. doorIndex, Vector3.new(10, 12, 1), Vector3.new(x, 8, z), purple)
        door.CFrame = CFrame.new(x, 8, z) * CFrame.Angles(0, math.pi, 0)
        label(door, question[2][doorIndex])
    end
    for _, x in ipairs({-21, -7, 7, 21}) do
        part(floor, "Pillar", Vector3.new(4, 25, 2), Vector3.new(x, 14, z))
    end
    part(floor, "Header", Vector3.new(44, 12, 2), Vector3.new(0, 20, z))
    local sign = part(floor, "Sign", Vector3.new(34, 4, 0.6), Vector3.new(0, 17, z + 1.4), Color3.fromRGB(17, 24, 42))
    sign.CFrame = CFrame.new(sign.Position) * CFrame.Angles(0, math.pi, 0)
    label(sign, question[1], cyan)
    local source = sources.MathDoorScript
    source = source:gsub('local QUESTION = "7 x 8 = %?"', 'local QUESTION = "' .. question[1] .. '"')
    for n = 1, 3 do source = source:gsub('local OPTION_' .. n .. ' = "[^"]+"', 'local OPTION_' .. n .. ' = "' .. question[2][n] .. '"') end
    source = source:gsub("local CORRECT_DOOR_INDEX = 2", "local CORRECT_DOOR_INDEX = " .. question[3])
    source = source:gsub("local STAGE_NUMBER = 1", "local STAGE_NUMBER = " .. i)
    source = source:gsub("local NEXT_STAGE = 2", "local NEXT_STAGE = " .. (i + 1))
    addScript(floor, "MathDoorScript", "Script", source)
    for _, x in ipairs({-11, 11}) do
        local gem = part(map, "Gem" .. i .. (x < 0 and "L" or "R"), Vector3.new(2, 3, 2), Vector3.new(x, 5, z + 12), cyan)
        gem.CFrame *= CFrame.Angles(0, 0, math.rad(35))
        addScript(gem, "CollectibleCoin", "Script", sources.CollectibleCoin)
    end
end
local finish = part(map, "FinishSign", Vector3.new(32, 6, 1), Vector3.new(0, 10, -124), Color3.fromRGB(17, 24, 42))
finish.CFrame *= CFrame.Angles(0, math.pi, 0)
label(finish, "META!\n3 pytania · 150 monet", Color3.fromRGB(255, 214, 90))
local intro = part(map, "Instructions", Vector3.new(16, 6, 1), Vector3.new(-13, 7, 17), Color3.fromRGB(17, 24, 42))
label(intro, "MATH CITY\nWybierz drzwi z wynikiem\nBłąd = powrót do checkpointu", cyan)
addScript(SSS, "LeaderstatsAndDataStore", "Script", sources.LeaderstatsAndDataStore)
addScript(SSS, "AdminServer", "Script", sources.AdminServer)
addScript(starter, "AdminPanelGui", "LocalScript", sources.AdminPanelGui)
local lighting = game:GetService("Lighting")
lighting.ClockTime, lighting.Brightness, lighting.Ambient = 14, 2, Color3.fromRGB(135, 145, 175)
workspace.CurrentCamera.CFrame = CFrame.lookAt(Vector3.new(40, 42, 40), Vector3.new(0, 5, -30))
game:GetService("ChangeHistoryService"):SetWaypoint("Dodano Math City")
print("MATMA_IMPORT_OK: 3 etapy, 9 drzwi, 4 checkpointy, 6 kryształów i panel administratora")
