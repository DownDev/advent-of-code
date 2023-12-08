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

current_node = "AAA"
required_steps = 0
while True:
    required_steps += 1

    instruction = 0 if next(instructions) == "L" else 1
    current = tree[current_node][instruction]

    if current == "ZZZ":
        break

    current_node = current

print(required_steps)
