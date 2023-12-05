from itertools import groupby

with open("input.txt") as f:
    lines = f.read().splitlines()

groups = [tuple(group) for not_empty, group in groupby(lines, bool) if not_empty]

seeds, *categories = groups
seeds_numbers = tuple(map(int, seeds[0].split()[1:]))
for category in categories:
    ranges = [tuple(map(int, numbers.split())) for numbers in category[1:]]

    sources = []
    for seed in seeds_numbers:
        for destination, source, length in ranges:
            if seed in range(source, source + length):
                sources.append(seed - source + destination)
                break
        else:
            sources.append(seed)

    seeds_numbers = sources

print(min(seeds_numbers))
