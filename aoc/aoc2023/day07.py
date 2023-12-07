import enum
from collections import Counter

from aoc import utils

# EXAMPLE = True
EXAMPLE = False

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
    def __init__(self, cards, wild=False):
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

    def __repr__(self):
        return f"Card({str(self.values)} [{self.type}]"

    def __eq__(self, other):
        return self.values == other.values

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        return self.values < other.values


def load_data():
    data = utils.load_data(2023, 7, example=EXAMPLE, fn=lambda s: s.split())

    return data


with utils.timed("Load data"):
    DATA = load_data()


def part1() -> int:
    result = 0

    hands = []
    for cards, bid in DATA:
        hands.append((Hand(cards), int(bid)))

    for rank, (hand, bid) in enumerate(sorted(hands), start=1):
        result += rank * bid

    return result


def part2() -> int:
    result = 0

    hands = []
    for cards, bid in DATA:
        hands.append((Hand(cards, wild=True), int(bid)))

    for rank, (hand, bid) in enumerate(sorted(hands), start=1):
        result += rank * bid

    return result


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
