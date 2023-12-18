import sys
import re
from collections import defaultdict

input = open("input").read().strip()
every_lines = input.split('\n')

answer_p1 = 0
answer_p2 = 0
dict_p2 = defaultdict(int)

for index, line in enumerate(every_lines):
    dict_p2[index] += 1
    before_pipe, after_pipe = line.split('|')
    id_, winning_list = before_pipe.split(':')
    winning_nums = [int(x) for x in winning_list.split()]
    having_nums = [int(x) for x in after_pipe.split()]

    val = len(set(winning_nums) & set(having_nums))
    if val > 0:
        answer_p1 += 2 ** (val - 1)
    for j in range(val):
        dict_p2[index+1+j] += dict_p2[index]

print(answer_p1)
print(sum(dict_p2.values()))