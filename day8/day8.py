import re
from collections import Counter
from functools import cmp_to_key
from itertools import cycle

input_day8 = open("input").read().strip()


# print(input_day8)

def part1(input_string):
    directions, connections = input_string.split('\n\n')
    directions = cycle('L' if d == 'L' else 'R' for d in directions) #Boucle inf!


    # print(connections)
    road_to_follow = {'L': {}, 'R': {}}
    for line in connections.split('\n'):
        source, left_right_destination = line.split('=')
        source = source.strip()
        left_destination, right_destination = left_right_destination.split(",")
        left = left_destination.strip()[1:].strip()
        right = right_destination[:-1].strip()

        road_to_follow['L'][source] = left
        road_to_follow['R'][source] = right

    # print(road_to_follow)
    node = 'AAA'
    for steps, direction in enumerate(directions, start=1):
        node = road_to_follow[direction][node]
        if node == 'ZZZ':
            break

    return steps


def part2(input_list):
    pass


print(part1(input_day8))
# print(part2(input_day7))
