from collections import deque

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = {
    "|": {LEFT: (DOWN, UP), RIGHT: (DOWN, UP)},
    "-": {UP: (LEFT, RIGHT), DOWN: (LEFT, RIGHT)},
    "/": {UP: (RIGHT,), DOWN: (LEFT,), LEFT: (DOWN,), RIGHT: (UP,)},
    "\\": {UP: (LEFT,), DOWN: (RIGHT,), LEFT: (UP,), RIGHT: (DOWN,)},
    ".": {},
}

with open("input.txt") as f:
    lines = f.read().splitlines()

queue = deque([(0, -1, *RIGHT)])
seen = set()

while queue:
    row, column, dr, dc = queue.popleft()
    new_row = row + dr
    new_column = column + dc

    if (
        new_row < 0
        or new_row >= len(lines)
        or new_column < 0
        or new_column >= len(lines[0])
    ):
        continue

    for new_directions in DIRECTIONS[lines[new_row][new_column]].get(
        (dr, dc), ((dr, dc),)
    ):
        if (new_row, new_column, *new_directions) not in seen:
            queue.append((new_row, new_column, *new_directions))
            seen.add((new_row, new_column, *new_directions))

print(len({(row, column) for row, column, *_ in seen}))
