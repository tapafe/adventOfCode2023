import sys
import re
from collections import defaultdict

input = open("input").read().strip()
every_lines = input.split('\n')

answer_p1 = 0
answer_p1_list = []
answer_p2 = 0

matrix = []

for lines in every_lines:
    lines_char = []
    for char in lines:
        lines_char.append(char)
    matrix.append(lines_char)

len_matrix = len(matrix)
len_char = len(matrix[0])

nums = defaultdict(list)
for lines in range(len(matrix)):
    gears = set()
    part_numbers = False
    number = 0
    for char in range(len(matrix[lines]) + 1):
        if char < len_char and matrix[lines][char].isdigit():
            number = number * 10 + int(matrix[lines][char])
            for abscissa in [-1, 0, 1]:  # For Matrix
                for ordinate in [-1, 0, 1]:  # For Char
                    if 0 <= lines + abscissa < len(matrix) and 0 <= char + ordinate < len(matrix[0]):
                        char_to_check = matrix[lines + abscissa][char + ordinate]
                        if char_to_check != '.' and not char_to_check.isdigit():
                            part_numbers = True
                        if char_to_check == '*':
                            gears.add((lines + abscissa, char + ordinate))

        elif number > 0:
            for gear in gears:
                nums[gear].append(number)
            if part_numbers:
                answer_p1 += number
                answer_p1_list.append(number)

            part_numbers = False
            number = 0
            gears = set()

print(answer_p1)
for k, v in nums.items():
    if len(v) == 2:
        answer_p2 += v[0] * v[1]
print(answer_p2)
