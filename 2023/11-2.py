import itertools

with open("input.txt") as f:
    lines = f.read().splitlines()

empty_rows = [i for i, row in enumerate(lines) if set(row) == {"."}]
empty_cols = [i for i, col in enumerate(zip(*lines)) if set(col) == {"."}]

galaxies = [
    (i, j) for i, row in enumerate(lines) for j, char in enumerate(row) if char == "#"
]

res = 0
for (a1, b1), (a2, b2) in itertools.combinations(galaxies, 2):
    for r in range(*sorted((a1, a2))):
        res += 1 + (999_999 * (r in empty_rows))
    for c in range(*sorted((b1, b2))):
        res += 1 + (999_999 * (c in empty_cols))

print(res)
