input = open("input").read().strip()
input_list = input.split('\n')

answer_p1 = 0
answer_p2 = 0

# p1
for line in input_list:
    p1_digit = []
    for char in line:
        if char.isdigit():
            p1_digit.append(str(char))
            break
    for char in reversed(line):
        if char.isdigit():
            p1_digit.append(str(char))
            break
    answer_p1 += int(p1_digit[0] + p1_digit[-1])

# p2
for line in input_list:
    p2_digit = []
    for index, char in enumerate(line):
        if char.isdigit():
            p2_digit.append(str(char))
        for digit_index, value in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], 1):
            if line[index:].startswith(value):
                p2_digit.append(str(digit_index))

    answer_p2 += int(p2_digit[0] + p2_digit[-1])

print(answer_p1)
print(answer_p2)
