input_day9 = open("input").read().splitlines()


# print(input_day8)

def extrapolate_right(history_input):
    if all(value == 0 for value in history_input):
        return 0
    else:
        diff = [history_input[i + 1] - history_input[i] for i in range(len(history_input) - 1)]
        return history_input[-1] + extrapolate_right(diff)

def extrapolate_left(history_input):
    if all(value == 0 for value in history_input):
        return 0
    else:
        diff = [history_input[i + 1] - history_input[i] for i in range(len(history_input) - 1)]
        return history_input[0] - extrapolate_left(diff)


def part1(input_string):
    total = 0
    for line in input_string:
        history = [int(num) for num in line.split()]
        total += extrapolate_right(history)

    return total


def part2(input_string):
    total = 0
    for line in input_string:
        history = [int(num) for num in line.split()]
        total += extrapolate_left(history)

    return total


print(part1(input_day9))
print(part2(input_day9))
