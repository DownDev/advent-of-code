with open("input.txt") as f:
    lines = f.read().splitlines()

res = 0
for line in lines:
    first, my_numbers = line.split(" | ")
    _, winning = first.split(": ")

    winning_list = winning.split()
    my_numbers_list = my_numbers.split()

    matches_value = 0
    for number in my_numbers_list:
        if number in winning_list:
            if not matches_value:
                matches_value = 1
            else:
                matches_value *= 2

    res += matches_value
print(res)
