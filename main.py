import random
import state
from state import State
from box import Box

# stack_A = [
#     Box(15, 50, 30),
#     Box(4, 4, 4),
#     Box(20, 70, 30),
#     Box(15, 45, 20),
#     Box(15, 60, 30),
#     Box(25, 60, 40),
#     Box(5, 10, 10),
#     Box(5, 20, 10),
#     Box(15, 30, 15)
# ]

stack_A = [
    Box(15, 50, 30),
    Box(4, 4, 4),
    Box(20, 70, 30),
    Box(15, 45, 20)
]

random.shuffle(stack_A)

root_state = State(0, None, {
    "Stack A": stack_A,
    "Stack B": [],
    "Stack C": []
})

state.create_state_tree(root_state)

# Start PEAS cycle

# 1 - Percieve

# 2 - Think

# 3 - Act
