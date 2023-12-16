from collections import deque

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

DIRECTIONS = {
    "|": {LEFT: (UP, DOWN), RIGHT: (UP, DOWN)},
    "-": {UP: (LEFT, RIGHT), DOWN: (LEFT, RIGHT)},
    "/": {UP: (RIGHT,), DOWN: (LEFT,), LEFT: (DOWN,), RIGHT: (UP,)},
    "\\": {UP: (LEFT,), DOWN: (RIGHT,), LEFT: (UP,), RIGHT: (DOWN,)},
    ".": {},
}


def get_energized_tiles(row, column, dr, dc):
    queue = deque([(row, column, dr, dc)])
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

        for new_direction in DIRECTIONS[lines[new_row][new_column]].get(
            (dr, dc), ((dr, dc),)
        ):
            if (new_row, new_column, *new_direction) not in seen:
                queue.append((new_row, new_column, *new_direction))
                seen.add((new_row, new_column, *new_direction))

    return len({(row, column) for row, column, *_ in seen})


with open("input.txt") as f:
    lines = f.read().splitlines()

print(
    max(
        [
            max(
                get_energized_tiles(i, -1, *RIGHT),
                get_energized_tiles(i, len(lines[0]), *LEFT),
            )
            for i in range(len(lines))
        ]
        + [
            max(
                get_energized_tiles(-1, i, *DOWN),
                get_energized_tiles(len(lines), i, *UP),
            )
            for i in range(len(lines[0]))
        ]
    )
)
