from itertools import groupby
from operator import gt, lt

OPERATORS = {"<": lt, ">": gt}

with open("input.txt") as f:
    lines = f.read().splitlines()

workflows_raw, ratings = [
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


def check_rules(items, name="in"):
    if name == "R":
        return False

    if name == "A":
        return True

    rules, fallback = workflows[name]

    for key, comparsion, value, target in rules:
        if OPERATORS[comparsion](items[key], value):
            return check_rules(items, target)

    return check_rules(items, fallback)


res = 0
for rating in ratings:
    items = {
        key: int(value)
        for expression in rating[1:-1].split(",")
        for key, value in [expression.split("=")]
    }
    if check_rules(items):
        res += sum(items.values())

print(res)
