from itertools import groupby


def find_mirror(group):
    for i in range(1, len(group)):
        above = group[:i][::-1]
        below = group[i:]

        if all(a == b for a, b in zip(above, below)):
            return i

    return 0


with open("input.txt") as f:
    lines = f.read().splitlines()

groups = [tuple(group) for not_empty, group in groupby(lines, bool) if not_empty]

res = 0
for group in groups:
    res += find_mirror(group) * 100
    res += find_mirror(tuple(zip(*group)))

print(res)
