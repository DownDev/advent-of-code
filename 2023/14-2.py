with open("input.txt") as f:
    lines = tuple(f.read().splitlines())


def rotate(lines):
    for _ in range(4):
        lines = map("".join, zip(*lines))
        lines = (
            "#".join("".join(sorted(group, reverse=True)) for group in line.split("#"))
            for line in lines
        )
        lines = tuple(line[::-1] for line in lines)

    return lines


history = {}

for i in range(1_000_000_000):
    if lines in history:
        break
    history[lines] = i
    history[i] = lines
    lines = rotate(lines)

offset = history[lines]

print(
    sum(
        row.count("O") * (len(lines) - i)
        for i, row in enumerate(
            history[(1_000_000_000 - offset) % (len(history) / 2 - offset) + offset]
        )
    )
)
