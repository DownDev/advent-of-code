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

low = 1000
high = 0

for _ in range(1000):
    queue = deque(["broadcaster", target, False] for target in broadcaster)

    while queue:
        name, target, pulse = queue.popleft()

        if pulse:
            high += 1
        else:
            low += 1

        if target not in modules:
            continue

        module = modules[target]

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

print(low * high)
