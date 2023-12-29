from dataclasses import dataclass
from operator import attrgetter


@dataclass
class Brick:
    x1: int
    y1: int
    z1: int
    x2: int
    y2: int
    z2: int


with open("input.txt") as f:
    lines = f.read().splitlines()


def overlaps(a, b):
    return max(a.x1, b.x1) <= min(a.x2, b.x2) and max(a.y1, b.y1) <= min(a.y2, b.y2)


bricks = sorted(
    (Brick(*map(int, line.replace("~", ",").split(","))) for line in lines),
    key=attrgetter("z1"),
)

for i, brick in enumerate(bricks):
    max_z = max(
        (above.z2 + 1 for above in bricks[:i] if overlaps(brick, above)), default=1
    )
    brick.z2 -= brick.z1 - max_z
    brick.z1 = max_z

bricks_above = {i: set() for i in range(len(bricks))}
bricks_below = {i: set() for i in range(len(bricks))}

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if overlaps(lower, upper) and upper.z1 == lower.z2 + 1:
            bricks_above[i].add(j)
            bricks_below[j].add(i)

print(
    sum(
        all(len(bricks_below[j]) >= 2 for j in bricks_above[i])
        for i in range(len(bricks))
    )
)
