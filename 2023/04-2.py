with open("input.txt") as f:
    lines = f.read().splitlines()

scratches = [1] * len(lines)
for i, line in enumerate(lines):
    first, my_numbers = line.split(" | ")
    _, winning = first.split(": ")

    winning_list = winning.split()
    my_numbers_list = my_numbers.split()

    total_matches = 0
    for number in my_numbers_list:
        if number in winning_list:
            total_matches += 1
            scratches[i + total_matches] += scratches[i]

print(sum(scratches))
