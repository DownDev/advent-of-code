DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open("input.txt") as f:
    lines = f.read().splitlines()

points = [(0, 0)]
boundary = 0

for line in lines:
    *_, color = line.split()
    instructions = color[2:-1]
    dr, dc = DIRECTIONS[int(instructions[-1])]
    steps = int(instructions[:-1], 16)
    boundary += steps
    row, column = points[-1]
    points.append((row + dr * steps, column + dc * steps))

print(
    abs(
        sum(
            x1 * y2 - x2 * y1
            for (x1, y1), (x2, y2) in zip(points, points[1:] + points[:1])
        )
    )
    // 2
    + boundary // 2
    + 1
)
