--[[
    Skrypt: MathDoorScript.luau
    Gdzie wkleić: Wewnątrz modelu danego piętra w Workspace (np. Workspace -> Floor1 -> Script)

    Struktura modelu w Workspace:
    Model "Floor1":
       ├── Sign (Klocek z tablicą nad drzwiami)
       ├── Door1 (Klocek pierwszych drzwi)
       ├── Door2 (Klocek drugich drzwi)
       ├── Door3 (Klocek trzecich drzwi)
       └── MathDoorScript (ten skrypt)
--]]

local floorModel = script.Parent

-- ================= KONFIGURACJA PIĘTRA =================
local QUESTION = "7 x 8 = ?"
local OPTION_1 = "48"
local OPTION_2 = "56" -- Poprawna odpowiedź!
local OPTION_3 = "64"
local CORRECT_DOOR_INDEX = 2 -- Które drzwi są poprawne (1, 2 lub 3)
local STAGE_NUMBER = 1 -- Numer bieżącego piętra
local NEXT_STAGE = 2   -- Numer kolejnego piętra
local COIN_REWARD = 50 -- Ile monet za przejście piętra
-- =======================================================

local sign = floorModel:FindFirstChild("Sign")
local door1 = floorModel:FindFirstChild("Door1")
local door2 = floorModel:FindFirstChild("Door2")
local door3 = floorModel:FindFirstChild("Door3")

local doors = {door1, door2, door3}
local options = {OPTION_1, OPTION_2, OPTION_3}
assert(door1 and door2 and door3, "Piętro wymaga Door1, Door2 i Door3")

-- Funkcja pomocnicza: tworzenie ładnego tekstu 3D / SurfaceGui na klocku
local function attachText(part, text, textColor, textSize)
    if not part then return end

    local gui = part:FindFirstChild("SurfaceGui")
    if not gui then
        gui = Instance.new("SurfaceGui")
        gui.Face = Enum.NormalId.Front
        gui.AlwaysOnTop = true
        gui.Parent = part
    end

    local label = gui:FindFirstChild("TextLabel")
    if not label then
        label = Instance.new("TextLabel")
        label.Size = UDim2.new(1, 0, 1, 0)
        label.BackgroundTransparency = 1
        label.Font = Enum.Font.FredokaOne
        label.TextScaled = true
        label.Parent = gui
    end

    label.Text = tostring(text)
    label.TextColor3 = textColor or Color3.fromRGB(255, 255, 255)
end

-- Ustawiamy pytanie na tablicy
if sign then
    attachText(sign, QUESTION, Color3.fromRGB(255, 255, 0))
end

-- Ustawiamy napisy na drzwiach
for i, door in ipairs(doors) do
    if door then
        attachText(door, options[i], Color3.fromRGB(255, 255, 255))
        door.Material = Enum.Material.SmoothPlastic
        door.CanCollide = true
    end
end

-- Obsługa dotknięcia drzwi
for i, door in ipairs(doors) do
    if not door then continue end

    local isCorrect = (i == CORRECT_DOOR_INDEX)
    local originalColor = door.Color
    local originalTransparency = door.Transparency
    local closeVersion = 0

    door.Touched:Connect(function(hit)
        local character = hit.Parent
        local player = game.Players:GetPlayerFromCharacter(character)
        if not player then return end
        if player:GetAttribute("DataLoaded") ~= true then return end

        local humanoid = character:FindFirstChild("Humanoid")
        if not humanoid or humanoid.Health <= 0 then return end

        if isCorrect then
            -- POPRAWNA ODPOWIEDŹ:
            -- Drzwi stają się zielone i przepuszczają gracza!
            door.CanCollide = false
            door.Transparency = 0.5
            door.Color = Color3.fromRGB(50, 220, 50)

            -- Aktualizacja postępu w leaderstats
            local leaderstats = player:FindFirstChild("leaderstats")
            if leaderstats then
                local stageStat = leaderstats:FindFirstChild("Stage")
                local coinsStat = leaderstats:FindFirstChild("Coins")

                if stageStat and stageStat.Value == STAGE_NUMBER then
                    stageStat.Value = NEXT_STAGE
                    if coinsStat then
                        coinsStat.Value = math.min(1000000000, coinsStat.Value + COIN_REWARD)
                    end
                end
            end

            -- Po 3 sekundach drzwi znów stają się twarde dla kolejnych graczy
            closeVersion += 1
            local version = closeVersion
            task.delay(3, function()
                if version ~= closeVersion or not door.Parent then return end
                door.CanCollide = true
                door.Transparency = originalTransparency
                door.Color = originalColor
            end)
        else
            -- BŁĘDNA ODPOWIEDŹ:
            -- Sprawdzamy czy gracz ma włączony God Mode (z Admin Panelu)
            local hasGodMode = player:GetAttribute("GodMode") == true
            if not hasGodMode then
                -- Dotknięcie złych drzwi = ŚMIERĆ!
                humanoid.Health = 0
            end
        end
    end)
end
