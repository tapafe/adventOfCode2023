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

    min_location = float('inf')
    while seeds_intervals:

        x1, x2, level = seeds_intervals.pop()

        if level == 8:  # level 8 correspond humidity-to-location map:
            min_location = min(x1, min_location)
            continue

        for conversion in re.findall(r'(\d+) (\d+) (\d+)', input[level]):
            z, y1, dy = map(int, conversion)
            y2 = y1 + dy
            diff = z - y1
            if x2 <= y1 or y2 <= x1:  # no overlap
                continue
            if x1 < y1:  # split original interval at y1
                seeds_intervals.append((x1, y1, level))
                x1 = y1
            if y2 < x2:  # split original interval at y2
                seeds_intervals.append((y2, x2, level))
                x2 = y2
            seeds_intervals.append(
                (x1 + diff, x2 + diff, level + 1))  # perfect overlap -> make conversion and let pass to next nevel
            break

        else:
            seeds_intervals.append((x1, x2, level + 1))

    return min_location


# print(part1(open("input").read().strip()))
print(part2(open("input").read().strip()))
