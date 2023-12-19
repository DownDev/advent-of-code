import math
from itertools import groupby

with open("input.txt") as f:
    lines = f.read().splitlines()

workflows_raw, _ = [
    tuple(group) for not_empty, group in groupby(lines, bool) if not_empty
]

workflows = {}
for workflow in workflows_raw:
    name, rules_str = workflow[:-1].split("{")
    rules = rules_str.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        condition, target = rule.split(":")
        key, comparsion, *value = tuple(condition)
        workflows[name][0].append((key, comparsion, int("".join(value)), target))


def count_ranges(ranges, name="in"):
    if name == "R":
        return 0

    if name == "A":
        return math.prod(stop - start + 1 for start, stop in ranges.values())

    rules, fallback = workflows[name]
    total = 0
    for key, comparsion, value, target in rules:
        start, stop = ranges[key]

        if comparsion == "<":
            t_start, t_stop = start, value - 1
            f_start, f_stop = value, stop
        else:
            t_start, t_stop = value + 1, stop
            f_start, f_stop = start, value

        if t_start <= t_stop:
            total += count_ranges({**ranges, key: (t_start, t_stop)}, target)
        if f_start <= f_stop:
            ranges[key] = (f_start, f_stop)
        else:
            break
    else:
        total += count_ranges(ranges, fallback)

    return total


print(count_ranges({category: (1, 4000) for category in "xmas"}))
