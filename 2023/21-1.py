from collections import deque

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

with open("input.txt") as f:
    data = f.read()
    lines = data.splitlines()
    S = divmod(data.find("S"), len(lines) + 1)

queue = deque([(*S, 64)])
seen = {S}
res = 0

while queue:
    row, column, steps = queue.popleft()

    if not steps & 1:
        res += 1

    if not steps:
        continue

    for dr, dc in DIRECTIONS:
        new_row = row + dr
        new_column = column + dc
        if (
            new_row < 0
            or new_row >= len(lines)
            or new_column < 0
            or new_column >= len(lines[0])
            or lines[new_row][new_column] == "#"
            or (new_row, new_column) in seen
        ):
            continue

        queue.append((new_row, new_column, steps - 1))
        seen.add((new_row, new_column))

print(res)
