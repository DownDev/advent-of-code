from functools import cache

with open("input.txt") as f:
    lines = f.read().splitlines()


@cache
def check_pattern(line, numbers):
    if not line:
        return not numbers

    if not numbers:
        return "#" not in line

    res = 0

    if line[0] in ".?":
        res += check_pattern(line[1:], numbers)

    if line[0] in "#?":
        if (
            numbers[0] <= len(line)
            and "." not in line[: numbers[0]]
            and (numbers[0] == len(line) or line[numbers[0]] != "#")
        ):
            res += check_pattern(line[numbers[0] + 1 :], numbers[1:])

    return res


res = 0
for line in lines:
    spring, condition = line.split()
    condition = tuple(map(int, condition.split(",")))
    res += check_pattern("?".join([spring] * 5), condition * 5)

print(res)
