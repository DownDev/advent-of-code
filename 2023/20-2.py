import math
from collections import deque

with open("input.txt") as f:
    lines = f.read().splitlines()

modules = {}
broadcaster = []
for line in lines:
    left, right = line.split(" -> ")
    destinations = right.split(", ")
    if left == "broadcaster":
        broadcaster = destinations
        continue

    module_type = left[0]
    module_name = left[1:]
    modules[module_name] = [
        module_type,
        False if module_type == "%" else {},
        destinations,
    ]

for name, (_, _, destinations) in modules.items():
    for destination in destinations:
        if destination in modules and modules[destination][0] == "&":
            modules[destination][1][name] = False

(outputs_rx,) = [
    name for name, (_, _, destinations) in modules.items() if "rx" in destinations
]
keys = (
    name for name, (_, _, destinations) in modules.items() if outputs_rx in destinations
)
seen = dict.fromkeys(keys, False)
cycles = dict.fromkeys(keys, 0)
presses = 0

while True:
    presses += 1
    queue = deque(["broadcaster", target, False] for target in broadcaster)

    while queue:
        name, target, pulse = queue.popleft()

        if target not in modules:
            continue

        module = modules[target]

        if target == outputs_rx and pulse:
            seen[name] = True
            cycles[name] = presses

            if all(seen.values()):
                break

        if module[0] == "%":
            if pulse:
                continue

            module[1] = not module[1]
            new_pulse = module[1]
        else:
            module[1][name] = pulse
            new_pulse = not all(module[1].values())

        for destination in module[2]:
            queue.append((target, destination, new_pulse))

    else:
        continue
    break

print(math.lcm(*cycles.values()))
