with open("input.txt") as f:
    lines = f.read().splitlines()

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

MAX_AMOUNTS = {"red": RED_MAX, "green": GREEN_MAX, "blue": BLUE_MAX}

res = 0

for line in lines:
    game, cubes_all = line.split(":")
    cubes_groups = cubes_all.split(";")

    game_possibilities = []
    for group in cubes_groups:
        amounts = {"red": 0, "green": 0, "blue": 0}
        cubes = group.split(",")
        for cube in cubes:
            amount, color = cube.strip().split()
            amounts[color] += int(amount)

        game_possibilities.append(
            all((MAX_AMOUNTS[color] >= amount for color, amount in amounts.items()))
        )

    if all(game_possibilities):
        res += int(game.split()[-1])

print(res)
