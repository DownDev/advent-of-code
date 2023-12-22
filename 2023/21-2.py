from collections import deque

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

with open("input.txt") as f:
    data = f.read()
    lines = data.splitlines()
    rows = len(lines)
    columns = len(lines[0])
    S = divmod(data.find("S"), rows + 1)


def loop(steps):
    queue = deque([(*S, steps, 0, 0)])
    seen = {(*S, 0, 0)}
    res = 0

    while queue:
        row, column, steps, row_wraps, col_wraps = queue.popleft()

        if not steps & 1:
            res += 1

        if not steps:
            continue

        for dr, dc in DIRECTIONS:
            new_row_wraps, new_row = divmod(row + dr, rows)
            new_col_wraps, new_column = divmod(column + dc, columns)
            new_row_wraps += row_wraps
            new_col_wraps += col_wraps

            if (
                lines[new_row][new_column] == "#"
                or (new_row, new_column, new_row_wraps, new_col_wraps) in seen
            ):
                continue

            queue.append((new_row, new_column, steps - 1, new_row_wraps, new_col_wraps))
            seen.add((new_row, new_column, new_row_wraps, new_col_wraps))

    return res


n = 26501365 // rows
t1 = loop(S[0])
t2 = loop(S[0] + rows)
t3 = loop(S[0] + 2 * rows)

print((n**2 - n) * ((t3 + t1) // 2 - t2) + n * (t2 - t1) + t1)
