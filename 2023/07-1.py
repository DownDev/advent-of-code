from collections import Counter, defaultdict
from enum import IntEnum, auto
from operator import itemgetter

with open("input.txt") as f:
    lines = f.read().splitlines()


class HandType(IntEnum):
    FIVE_OF_A_KIND = auto()
    FOUR_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    THREE_OF_A_KIND = auto()
    TWO_PAIRS = auto()
    ONE_PAIR = auto()
    HIGH_CARD = auto()


CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def calculate_strength(hand):
    cards = Counter(hand)
    if len(cards) == 1:
        return HandType.FIVE_OF_A_KIND

    if len(cards) == 2:
        if 4 in cards.values():
            return HandType.FOUR_OF_A_KIND

        return HandType.FULL_HOUSE

    if len(cards) == 3:
        if 3 in cards.values():
            return HandType.THREE_OF_A_KIND

        return HandType.TWO_PAIRS

    if len(cards) == 4:
        return HandType.ONE_PAIR

    return HandType.HIGH_CARD


def compare_cards(cards):
    return [CARDS.index(card) for card in cards[0]]


strengths = defaultdict(list)

for line in lines:
    hand, bid = line.split()
    bid_number = int(bid)

    strengths[calculate_strength(hand)].append((hand, bid_number))

bids = []
for key in sorted(strengths):
    values = sorted(strengths[key], key=itemgetter(0))
    for value in sorted(values, key=compare_cards):
        bids.append(value[1])

print(sum(bid * i for i, bid in enumerate(reversed(bids), start=1)))
