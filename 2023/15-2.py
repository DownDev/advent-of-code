import re
from collections import defaultdict
from functools import reduce

with open("input.txt") as f:
    line = f.read()

boxes = defaultdict(list)
focal_lengths = {}

for label, operation, focal_length in re.findall(r"([a-z]+)([=-])(\d)?", line):
    hashed = reduce(lambda val, char: (val + ord(char)) * 17 % 256, label, 0)
    destination = boxes[hashed]
    if operation == "=":
        if label not in destination:
            destination.append(label)
        focal_lengths[label] = int(focal_length)
    else:
        destination.remove(label) if label in destination else None
        focal_lengths.pop(label) if label in focal_lengths else None

print(
    sum(
        (box_number + 1) * j * focal_lengths[label]
        for box_number, labels in boxes.items()
        for j, label in enumerate(labels, start=1)
    )
)
