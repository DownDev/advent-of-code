import operator
from functools import reduce

with open("input.txt") as f:
    lines = f.read().splitlines()

res = 0

for line in lines:
    game, cubes_all = line.split(":")
    cubes_groups = cubes_all.split(";")

    amounts = {"red": 1, "green": 1, "blue": 1}
    for group in cubes_groups:
        cubes = group.split(",")
        for cube in cubes:
            amount, color = cube.strip().split()
            amount = int(amount)
            if amounts[color] < amount:
                amounts[color] = amount

    res += reduce(operator.mul, amounts.values())

print(res)
