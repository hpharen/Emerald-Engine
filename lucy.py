import random
import time
import os

ACTIONS = ["A","B","Up","Down","Left","Right"]

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
