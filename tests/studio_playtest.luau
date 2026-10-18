-- Run in Studio's SERVER Command Bar during Play. Does not persist in the map.
assert(game:GetService("RunService"):IsStudio(), "Studio only")
assert(game:GetService("RunService"):IsServer(), "Use the Server tab")
task.spawn(function()
    local ok, err = pcall(function()
        local player = game.Players:GetPlayers()[1]
        assert(player and player:GetAttribute("DataLoaded"), "Player data not loaded")
        local stats = player.leaderstats
        local function check(condition, name)
            assert(condition, name)
            print("MATMA_TEST_PASS " .. name)
        end
        local function root()
            local char = player.Character
            assert(char and char:FindFirstChild("HumanoidRootPart"), "Character missing")
            return char.HumanoidRootPart, char.Humanoid
        end
        local function moveNear(position)
            local r, h = root()
            r.CFrame = CFrame.new(position)
            r.AssemblyLinearVelocity = Vector3.zero
            h:MoveTo(position)
            task.wait(0.3)
        end
        local function touchDoor(door)
            moveNear(Vector3.new(door.Position.X, 5.5, door.Position.Z + 4))
            local _, h = root()
            h:MoveTo(Vector3.new(door.Position.X, 5.5, door.Position.Z - 5))
            task.wait(2)
        end
        check(stats.Stage.Value == 1, "initial stage")
        local coinStart = stats.Coins.Value
        local gemStart = stats.Gems.Value
        -- Obsługuje również zapisaną mapę przed ręczną zmianą nazwy w Studio.
        local map = workspace:FindFirstChild("MathCity") or workspace:FindFirstChild("MathAdventure")
        assert(map, "Math City map missing")
        local gem = map.Gem1L
        moveNear(gem.Position + Vector3.new(0, 0, 3))
        local _, h = root()
        h:MoveTo(gem.Position)
        task.wait(1)
        check(stats.Gems.Value == gemStart + 1 and gem.Transparency == 1, "gem collection")
        touchDoor(map.Floor1.Door2)
        check(stats.Stage.Value == 2 and stats.Coins.Value == coinStart + 50, "correct door reward")
        moveNear(Vector3.new(0, 5.5, -32))
        task.wait(3.3)
        check(map.Floor1.Door2.CanCollide and map.Floor1.Door2.Color == Color3.fromRGB(162, 94, 255), "door reset")
        touchDoor(map.Floor1.Door2)
        check(stats.Coins.Value == coinStart + 50, "no duplicate reward")
        local oldCharacter = player.Character
        touchDoor(map.Floor2.Door2)
        check(oldCharacter.Humanoid.Health == 0, "wrong answer kills")
        local deadline = os.clock() + 12
        repeat task.wait(0.2) until player.Character ~= oldCharacter or os.clock() > deadline
        local newCharacter = player.Character
        assert(newCharacter ~= oldCharacter, "Respawn timeout")
        newCharacter:WaitForChild("HumanoidRootPart", 5)
        task.wait(0.8)
        local r = root()
        check((r.Position - workspace.Checkpoints["2"].Position).Magnitude < 8, "respawn checkpoint")
        check(player:GetAttribute("GodMode") == false and player:GetAttribute("SpeedEnabled") == false, "server modes reset")
        touchDoor(map.Floor2.Door1)
        check(stats.Stage.Value == 3, "second stage")
        touchDoor(map.Floor3.Door3)
        check(stats.Stage.Value == 4 and stats.Coins.Value == coinStart + 150, "finish and 150 coins")
        moveNear(Vector3.new(0, 5.5, -106))
        task.wait(3)
        check(gem.Transparency == 0, "gem respawn")
        print("MATMA_TEST_COMPLETE")
    end)
    if not ok then warn("MATMA_TEST_FAIL " .. tostring(err)) end
end)
