with open("input.txt") as f:
    lines = f.read().splitlines()

left = []
right = []

for line in lines:
    x, y = line.split()
    left.append(int(x))
    right.append(int(y))

res = 0
for x, y in zip(sorted(left), sorted(right)):
    res += abs(x - y)

print(res)
