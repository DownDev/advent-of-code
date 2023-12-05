from itertools import groupby

with open("input.txt") as f:
    lines = f.read().splitlines()

groups = [tuple(group) for not_empty, group in groupby(lines, bool) if not_empty]

seeds, *categories = groups
seeds_ranges = tuple(map(int, seeds[0].split()[1:]))
seeds_numbers = [
    (seeds_ranges[i], seeds_ranges[i] + seeds_ranges[i + 1])
    for i in range(0, len(seeds_ranges), 2)
]

for category in categories:
    ranges = [tuple(map(int, numbers.split())) for numbers in category[1:]]

    sources = []
    while seeds_numbers:
        start, end = seeds_numbers.pop()
        for destination, source, length in ranges:
            overlap_start = max(start, source)
            overlap_end = min(end, source + length)
            if overlap_start < overlap_end:
                sources.append(
                    (
                        overlap_start - source + destination,
                        overlap_end - source + destination,
                    )
                )
                if overlap_start > start:
                    seeds_numbers.append((start, overlap_start))
                if end > overlap_end:
                    seeds_numbers.append((overlap_end, end))
                break
        else:
            sources.append((start, end))

    seeds_numbers = sources

print(min(seeds_numbers)[0])
