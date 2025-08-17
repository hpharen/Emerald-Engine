local buttons = {'A','B','Up','Down','Left','Right'}
local hold_frames = 15  -- shorter hold for 1 tile movement

local input = {}        -- current buttons being pressed
local hold_counter = 0  -- frames left to hold current action

while true do
    -- Write game state
    local f = io.open("state.txt", "w")
    f:write(tostring(emu.framecount()))
    f:close()

    -- Only read new action if not currently holding a button
    if hold_counter == 0 then
        local f2 = io.open("action.txt","r")
        if f2 then
            local action = f2:read("*l")
            f2:close()
            os.remove("action.txt")  -- remove for next action

            -- Validate action
            local valid = false
            for _, b in ipairs(buttons) do
                if action == b then
                    valid = true
                    break
                end
            end

            -- Set input only if valid
            if valid then
                input = {}
                input[action] = true
                hold_counter = hold_frames
                print("Pressing:", action)
            else
                print("Ignoring invalid action:", action)
            end
        end
    end

    -- Apply current button input
    joypad.set(input)

    -- Count down hold frames
    if hold_counter > 0 then
        hold_counter = hold_counter - 1
        if hold_counter == 0 then
            input = {} -- release after short hold
        end
    end

    emu.frameadvance()
end
