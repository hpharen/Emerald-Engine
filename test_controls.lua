-- Simple BizHawk Lua script to test GBA controls
-- Works for Pokémon Emerald or any GBA game in BizHawk

-- Define a sequence of button presses to test
local inputs = {
    { A = true },                -- Press A
    { B = true },                -- Press B
    { Start = true },            -- Press Start
    { Select = true },           -- Press Select
    { Up = true },               -- Press Up
    { Down = true },             -- Press Down
    { Left = true },             -- Press Left
    { Right = true },            -- Press Right
    { L = true },                -- Press L
    { R = true },                -- Press R
}

-- Loop index
local i = 1

while true do
    -- Clear previous inputs
    local inputTable = {}

    -- Get the current test input
    local currentInput = inputs[i]

    -- Apply it to inputTable
    for button, state in pairs(currentInput) do
        inputTable[button] = state
    end

    -- Output to console what’s being pressed
    for button, state in pairs(inputTable) do
        if state then
            print("Pressing: " .. button)
        end
    end

    -- Set the joypad input for this frame
    joypad.set(inputTable)

    -- Advance a few frames so input registers
    emu.frameadvance()
    emu.frameadvance()
    emu.frameadvance()

    -- Release buttons after pressing (so it’s not held forever)
    joypad.set({})
    emu.frameadvance()

    -- Add a 1 second delay (~60 frames for GBA)
    for f = 1, 60 do
        emu.frameadvance()
    end

    -- Move to next input
    i = i + 1
    if i > #inputs then
        i = 1 -- loop back to start
    end
end
