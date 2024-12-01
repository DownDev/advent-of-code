with open("input.txt") as f:
    lines = f.read().splitlines()

left = []
right = []

for line in lines:
    x, y = line.split()
    left.append(int(x))
    right.append(int(y))

res = 0
for num in left:
    res += num * right.count(num)

print(res)
