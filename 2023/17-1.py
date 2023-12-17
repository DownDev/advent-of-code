from heapq import heappop, heappush

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

with open("input.txt") as f:
    lines = f.read().splitlines()

nodes = [tuple(map(int, line)) for line in lines]

queue = [(0, 0, 0, 0, 0, 0)]
seen = set()

while queue:
    heat_loss, row, column, dr, dc, n = heappop(queue)

    if row == len(nodes) - 1 and column == len(nodes[0]) - 1:
        print(heat_loss)
        break

    if (row, column, dr, dc, n) in seen:
        continue

    seen.add((row, column, dr, dc, n))

    if n < 3 and (dr, dc) != (0, 0):
        new_row = row + dr
        new_column = column + dc
        if 0 <= new_row < len(nodes) and 0 <= new_column < len(nodes[0]):
            heappush(
                queue,
                (
                    heat_loss + nodes[new_row][new_column],
                    new_row,
                    new_column,
                    dr,
                    dc,
                    n + 1,
                ),
            )

    for new_dr, new_dc in DIRECTIONS:
        if (new_dr, new_dc) in ((dr, dc), (-dr, -dc)):
            continue

        new_row = row + new_dr
        new_column = column + new_dc
        if (
            new_row < 0
            or new_row >= len(nodes)
            or new_column < 0
            or new_column >= len(nodes[0])
        ):
            continue

        heappush(
            queue,
            (
                heat_loss + nodes[new_row][new_column],
                new_row,
                new_column,
                new_dr,
                new_dc,
                1,
            ),
        )
