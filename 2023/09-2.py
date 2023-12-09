import operator

with open("input.txt") as f:
    lines = f.read().splitlines()


def get_difference(numbers):
    difference = tuple(map(operator.sub, numbers[1:], numbers[:-1]))

    if len(set(difference)) == 1:
        return numbers[-1] + difference[0]

    return numbers[-1] + get_difference(difference)


print(sum(get_difference(tuple(map(int, line.split()))[::-1]) for line in lines))
