import re
from collections import defaultdict

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


def check_star_index(row, col, num):
    if 0 <= row < rows and 0 <= col < cols:
        if lines[row][col] == "*":
            star_indexes[(row, col)].append(num)
            return True
    return False


with open("input.txt") as f:
    lines = f.read().splitlines()

rows = len(lines)
cols = len(lines[0])

star_indexes = defaultdict(list)

for i, line in enumerate(lines):
    indexes = re.finditer(r"\d+", line)
    for idx in indexes:
        first_index = idx.start()
        last_index = idx.end() - 1

        for dr, dc in DIRECTIONS:
            new_row = i + dr
            if check_star_index(new_row, first_index + dc, idx.group()):
                break
            if check_star_index(new_row, last_index + dc, idx.group()):
                break

print(sum(int(num[0]) * int(num[1]) for num in star_indexes.values() if len(num) == 2))
