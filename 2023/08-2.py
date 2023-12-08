import math
from itertools import cycle

with open("input.txt") as f:
    lines = f.read().splitlines()

steps, _, *nodes = lines
instructions = cycle(steps)

tree = {}
for node in nodes:
    parent, children = node.split(" = ")
    left, right = children[1:-1].split(", ")
    tree[parent] = (left, right)

current_nodes = [node for node in tree if node.endswith("A")]
steps = []
for node in current_nodes:
    required_steps = 0
    current_node = node
    while True:
        required_steps += 1

        instruction = 0 if next(instructions) == "L" else 1
        current = tree[current_node][instruction]

        if current.endswith("Z"):
            break

        current_node = current

    steps.append(required_steps)

print(math.lcm(*steps))
