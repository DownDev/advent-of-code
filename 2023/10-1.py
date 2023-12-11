from collections import deque

UP = "S|LJ"
DOWN = "S|F7"
LEFT = "S-J7"
RIGHT = "S-LF"

DIRECTIONS = [
    (-1, 0, (UP, DOWN)),
    (1, 0, (DOWN, UP)),
    (0, -1, (LEFT, RIGHT)),
    (0, 1, (RIGHT, LEFT)),
]

with open("input.txt") as f:
    data = f.read()
    lines = data.splitlines()
    S = divmod(data.find("S"), len(lines) + 1)

queue = deque([S])
loop = {S}

while queue:
    row, column = queue.popleft()
    char = lines[row][column]

    for dr, dc, dirs in DIRECTIONS:
        new_row = row + dr
        new_column = column + dc
        from_dir, to_dir = dirs
        if (
            char in from_dir
            and lines[new_row][new_column] in to_dir
            and (new_row, new_column) not in loop
        ):
            queue.append((new_row, new_column))
            loop.add((new_row, new_column))

print(len(loop) // 2)
