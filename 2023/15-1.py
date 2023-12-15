from functools import reduce

with open("input.txt") as f:
    line = f.read()

print(
    sum(
        reduce(lambda val, char: (val + ord(char)) * 17 % 256, item, 0)
        for item in line.split(",")
    )
)
