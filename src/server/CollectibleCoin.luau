--[[
    Skrypt: CollectibleCoin.luau
    Gdzie wkleić: Jako zwykły Script wewnątrz klocka monety lub kryształu w Workspace.
    Opis: Kryształ lewituje i obraca się. Po dotknięciu daje graczowi Kryształy (Gems)
          i znika na 15 sekund, po czym pojawia się ponownie!
--]]

local gemPart = script.Parent
local RESPAWN_TIME = 15 -- Czas odnowienia kryształu w sekundach
local GEMS_AMOUNT = 1   -- Ile kryształów daje ten przedmiot

local canCollect = true

-- Ustawienia wyglądu (neonowy świecący diament)
gemPart.Anchored = true
gemPart.CanCollide = false
gemPart.Material = Enum.Material.Neon
gemPart.Color = Color3.fromRGB(0, 200, 255)

-- Animacja powolnego obracania się
task.spawn(function()
    while true do
        gemPart.CFrame = gemPart.CFrame * CFrame.Angles(0, math.rad(2), 0)
        task.wait(0.03)
    end
end)

-- Dotknięcie przez gracza
gemPart.Touched:Connect(function(hit)
    if not canCollect then return end

    local character = hit.Parent
    local player = game.Players:GetPlayerFromCharacter(character)
    if not player then return end
    if player:GetAttribute("DataLoaded") ~= true then return end

    local leaderstats = player:FindFirstChild("leaderstats")
    if not leaderstats then return end

    local gems = leaderstats:FindFirstChild("Gems")
    if gems then
        canCollect = false
        gems.Value = math.min(1000000000, gems.Value + GEMS_AMOUNT)

        -- Ukrywamy kryształ
        gemPart.Transparency = 1

        -- Odczekaj i przywróć kryształ
        task.wait(RESPAWN_TIME)
        gemPart.Transparency = 0
        canCollect = true
    end
end)
