import sys
import re
from collections import defaultdict


def part1(input_file):
    input = input_file.split('\n\n')

    seeds = [int(x) for x in input[0].replace("seeds: ", "").split(" ")]

    min_location = float('inf')
    for x in map(int, seeds):
        for seg in input[1:]:
            for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
                destination, source, range_length = map(int, conversion)
                if x in range(source, source + range_length):
                    x += destination - source
                    break

        min_location = min(x, min_location)
    return min_location


def part2(input_file):
    input = input_file.split('\n\n')
    seeds_intervals = []

    for seed in re.findall(r'(\d+) (\d+)', input[0]):
        x1, dx = map(int, seed)
        x2 = x1 + dx
        seeds_intervals.append((x1, x2, 1))

    print(seeds_intervals)
    min_location = float('inf')

    while seeds_intervals:
        print(seeds_intervals)
        seeds_destination, seeds_source, level = seeds_intervals.pop()

        if level == 8: # level 8 correspond humidity-to-location map:
            print("azpkeazpaz")
            min_location = 1
            return min_location

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', input[level]):
            destination, source, range_length = map(int, conversion)
            y2 = source + range_length
            diff = destination - source

            seeds_intervals.append((seeds_destination + diff, seeds_source + diff, level + 1))


# print(part1(open("input").read().strip()))
part2(open("input").read().strip())
