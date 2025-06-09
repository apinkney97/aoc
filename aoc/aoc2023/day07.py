from __future__ import annotations

import enum
from collections import Counter

type Data = list[tuple[str, int]]

VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

WILD_VALUES = dict(VALUES)
WILD_VALUES["J"] = 1


class HandType(int, enum.Enum):
    high_card = 1
    one_pair = 2
    two_pair = 3
    three_of_a_kind = 4
    full_house = 5
    four_of_a_kind = 6
    five_of_a_kind = 7


class Hand:
    def __init__(self, cards: str, wild: bool = False) -> None:
        if wild:
            values = WILD_VALUES
        else:
            values = VALUES
        self.values = [values[c] for c in cards]
        groups = Counter(self.values)

        if 1 in groups:
            if len(groups) > 1:
                wildcards = groups.pop(1)
                best = sorted((count, value) for value, count in groups.items())[-1][1]
                groups[best] += wildcards

        biggest_group = max(groups.values())

        if biggest_group >= 5:
            self.type = HandType.five_of_a_kind

        elif biggest_group == 4:
            self.type = HandType.four_of_a_kind

        elif biggest_group == 3:
            if len(groups) == 2:
                self.type = HandType.full_house
            else:
                self.type = HandType.three_of_a_kind

        elif biggest_group == 2:
            if len(groups) == 3:
                self.type = HandType.two_pair
            else:
                self.type = HandType.one_pair

        else:
            self.type = HandType.high_card

    def __repr__(self) -> str:
        return f"Card({str(self.values)} [{self.type}]"

    def __eq__(self, other: Hand) -> bool:  # type: ignore [override]
        return self.values == other.values

    def __lt__(self, other: Hand) -> bool:
        if self.type != other.type:
            return self.type < other.type
        return self.values < other.values


def parse_data(data: list[str]) -> Data:
    parsed = []
    for line in data:
        parts = line.split()
        parsed.append((parts[0], int(parts[1])))

    return parsed


def part1(data: Data) -> int:
    result = 0

    hands = []
    for cards, bid in data:
        hands.append((Hand(cards), bid))

    for rank, (hand, bid) in enumerate(sorted(hands), start=1):
        result += rank * bid

    return result


def part2(data: Data) -> int:
    result = 0

    hands = []
    for cards, bid in data:
        hands.append((Hand(cards, wild=True), bid))

    for rank, (hand, bid) in enumerate(sorted(hands), start=1):
        result += rank * bid

    return result
