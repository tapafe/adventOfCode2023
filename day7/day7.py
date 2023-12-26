import re
from collections import Counter
from functools import cmp_to_key

input_day7 = open("input").read().strip().split('\n')


def part1(input_list):
    def get_hands_value(hand):

        counts = sorted(Counter(hand).values(), reverse=True)
        if counts[0] == 5:
            return 6
        if counts[0] == 4:
            return 5
        if counts[0] == 3 and counts[1] == 2:
            return 4
        if counts[0] == 3:
            return 3
        if counts[0] == 2 and counts[1] == 2:
            return 2
        if counts[0] == 2:
            return 1
        return 0

    def compare_fnc(a, b):

        cards = '23456789TJQKA'
        hand_value_a = get_hands_value(a[0])
        hand_value_b = get_hands_value(b[0])
        if hand_value_a > hand_value_b:
            return 1
        if hand_value_a < hand_value_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (cards.index(card_a) > cards.index(card_b))
            return 1 if a_wins else -1

    hands_list = []
    for hands in input_list:
        hand, bid = hands.split()
        hands_list.append((hand, bid))

    hands_list.sort(key=cmp_to_key(compare_fnc))

    total = 0
    for rank, (hand, bid) in enumerate(hands_list, start=1):
        total += rank * int(bid)
    return total


def part2(input_list):
    def get_hands_value(hand):

        jokers = hand.count('J')
        hand = [c for c in hand if c != 'J']
        counts = sorted(Counter(hand).values(), reverse=True)
        if not counts:
            counts = [0]
        if counts[0] + jokers == 5:
            return 6
        if counts[0] + jokers == 4:
            return 5
        if counts[0] + jokers == 3 and counts[1] == 2:
            return 4
        if counts[0] + jokers == 3:
            return 3
        if counts[0] == 2 and counts[1] == 2:
            return 2
        if counts[0] == 2 or jokers:
            return 1
        return 0

    def compare_fnc(a, b):

        cards = 'J23456789TQKA'
        hand_value_a = get_hands_value(a[0])
        hand_value_b = get_hands_value(b[0])
        if hand_value_a > hand_value_b:
            return 1
        if hand_value_a < hand_value_b:
            return -1
        for card_a, card_b in zip(a[0], b[0]):
            if card_a == card_b:
                continue
            a_wins = (cards.index(card_a) > cards.index(card_b))
            return 1 if a_wins else -1

    hands_list = []
    for hands in input_list:
        hand, bid = hands.split()
        hands_list.append((hand, bid))

    hands_list.sort(key=cmp_to_key(compare_fnc))

    total = 0
    for rank, (hand, bid) in enumerate(hands_list, start=1):
        total += rank * int(bid)
    return total


print(part1(input_day7))
print(part2(input_day7))
