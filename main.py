import random

import astaralgorithm
from box import Box
from state import HanoiState

start_stack = [
    Box(15, 50, 30),
    Box(4, 4, 4),
    Box(20, 70, 30),
    Box(15, 45, 20),
    Box(15, 60, 30),
    Box(25, 60, 40),
    Box(5, 10, 10),
    Box(5, 20, 10),
    Box(15, 30, 15)
]

random.shuffle(start_stack)

start_value = {
    "Stack A": start_stack,
    "Stack B": [],
    "Stack C": []
}

goal_stack = sorted(start_stack, reverse=True)

goal_value = {
    "Stack A": [],
    "Stack B": [],
    "Stack C": goal_stack
}

root_state = HanoiState(value=start_value, goal=goal_value)

print("Starting A* algorithm path search...")
path = astaralgorithm.get_solving_path(root_state)

for i, step in enumerate(path):
    print(f"\n\nStep {i}")
    string = ""
    for key in step:
        string += f"{key}: "
        for box in step[key]:
            string += str(box.get_volume()) + ", "
        string += "\n"
    print(string)
