with open("input.txt") as f:
    lines = f.read().splitlines()

time = int("".join(lines[0].split()[1:]))
distance = int("".join(lines[1].split()[1:]))

res = 0
for i in range(1, time):
    if i * (time - i) > distance:
        res += 1

print(res)
