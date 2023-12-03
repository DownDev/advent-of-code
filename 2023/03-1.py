import re
import string

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
SYMBOLS = set(string.punctuation) - set(".")


def check_symbol_adjacment(row, col):
    return 0 <= row < rows and 0 <= col < cols and lines[row][col] in SYMBOLS


with open("input.txt") as f:
    lines = f.read().splitlines()

rows = len(lines)
cols = len(lines[0])

res = 0

for i, line in enumerate(lines):
    indexes = re.finditer(r"\d+", line)
    for idx in indexes:
        first_index = idx.start()
        last_index = idx.end() - 1

        found = []
        for dr, dc in DIRECTIONS:
            new_row = i + dr
            found.append(check_symbol_adjacment(new_row, first_index + dc))
            found.append(check_symbol_adjacment(new_row, last_index + dc))

        if any(found):
            res += int(idx.group())

print(res)
