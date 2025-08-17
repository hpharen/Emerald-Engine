import os
import time
import random
import psutil
import win32gui
import win32process
bizhawk_path = r"C:\Users\Haren\Downloads\BizHawk-2.10-win-x64\EmuHawk.exe"
ACTIONS = ["A","B","Up","Down","Left","Right"]

def open_bizhawk():
    print("Opening Bizhawk...")
    os.startfile(bizhawk_path)

def bizhawk_window(pids):
    titles = []
    returnpid = 0
    def _enum_cb(hwnd, results):
        if win32gui.IsWindowVisible(hwnd):
            pid = win32process.GetWindowThreadProcessId(hwnd)[1] 
            if pids is None or pid in pids:
                nonlocal returnpid
                returnpid = pid
    win32gui.EnumWindows(_enum_cb, titles)
    return returnpid

program_name = "EmuHawk.exe"
timeout = time.time() + 120
isOpen = False

# Check if Bizhawk is open, otherwise open it
for process in psutil.process_iter():
    try:
        if process.name() == program_name:
            print("Bizhawk is open.")
            isOpen = True
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
else:
    print("Bizhawk is not open.")
    open_bizhawk()

while True:
    # Wait until state.txt exists
    if not os.path.exists("state.txt"):
        time.sleep(0.9)
        continue

    with open("state.txt","r") as f:
        state = f.read().strip()

    # Pick an action (replace with RL agent later)
    action = random.choice(ACTIONS)

    # Wait until Lua deletes previous action.txt
    while os.path.exists("action.txt"):
        time.sleep(1)

    # Write new action
    with open("action.txt","w") as f:
        f.write(action)
