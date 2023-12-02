mapping = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

with open("input.txt") as f:
    data = f.read()
    for name, value in mapping.items():
        data = data.replace(name, value)

    lines = data.splitlines()

res = 0
for line in lines:
    num = ""
    for char in line:
        if char.isdigit():
            num += char
            break

    for char in line[::-1]:
        if char.isdigit():
            num += char
            break

    res += int(num)

print(res)
