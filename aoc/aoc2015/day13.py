import re
from itertools import permutations

from aoc import utils


def parse_data(data):
    re_ = re.compile(
        r"(?P<name1>\w+) would (?P<action>\w+) (?P<n>\d+) happiness units by sitting next to (?P<name2>\w+)\."
    )
    data = utils.parse_data(data, fn=re_.fullmatch)
    scores = {}
    for row in data:
        score = int(row["n"]) * (-1 if row["action"] == "lose" else 1)
        scores.setdefault(row["name1"], {})[row["name2"]] = score
    return scores


def circular_arrangements(names):
    names = list(names)
    first = names[0]
    others = names[1:]
    seen = set()
    for p in permutations(others):
        if p not in seen and tuple(reversed(p)) not in seen:
            seen.add(p)
            yield first, *p


def max_happiness(data):
    max_h = 0
    for arrangement in circular_arrangements(data.keys()):
        happiness = 0
        for i, name in enumerate(arrangement):
            happiness += data[name][arrangement[i - 1]]
            happiness += data[name][arrangement[(i + 1) % len(arrangement)]]
        max_h = max(happiness, max_h)

    return max_h


def part1(data) -> int:
    return max_happiness(data)


def part2(data) -> int:
    others = list(data.keys())
    data["me"] = {name: 0 for name in others}
    for name in others:
        data[name]["me"] = 0
    return max_happiness(data)
