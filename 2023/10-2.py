from collections import deque

UP = set("S|LJ")
DOWN = set("S|F7")
LEFT = set("S-J7")
RIGHT = set("S-LF")

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

s_pipe = (UP | DOWN | LEFT) - {"S"}

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
            if char == "S":
                s_pipe &= from_dir

lines[S[0]] = lines[S[0]].replace("S", tuple(s_pipe)[0])

outside = set()

for i, line in enumerate(lines):
    within = False
    up = None
    for j, char in enumerate(line):
        if (i, j) in loop:
            if char == "|":
                within = not within
            elif char in "LF":
                up = char == "L"
            elif char in "7J":
                if char != ("J" if up else "7"):
                    within = not within
                up = None

        if not within:
            outside.add((i, j))

print(len(lines) * len(lines[0]) - len(outside | loop))
