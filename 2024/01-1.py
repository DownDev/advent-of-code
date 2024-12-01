with open("input.txt") as f:
    lines = f.read().splitlines()

left = []
right = []

for line in lines:
    x, y = line.split()
    left.append(int(x))
    right.append(int(y))

distances = []

for x, y in zip(sorted(left), sorted(right)):
    distances.append(abs(x - y))

print(sum(distances))
