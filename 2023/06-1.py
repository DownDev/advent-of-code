with open("input.txt") as f:
    lines = f.read().splitlines()

times = map(int, lines[0].split()[1:])
distances = map(int, lines[1].split()[1:])

time_to_distance = {time: distance for time, distance in zip(times, distances)}
res = 1
for time, distance in time_to_distance.items():
    possibilities = []
    for i in range(1, time):
        if i * (time - i) > distance:
            possibilities.append(1)
    res *= len(possibilities)

print(res)
