import re
from itertools import permutations

from aoc import utils

RE = re.compile(r"(?P<place_1>\w+) to (?P<place_2>\w+) = (?P<dist>\d+)")

DATA = utils.load_data(2015, 9, fn=RE.fullmatch)


def _get_key(place_1, place_2):
    return tuple(sorted([place_1, place_2]))


def _get_distance(cmp_fn):
    distances = {}
    places = set()
    for line in DATA:
        place_1 = line["place_1"]
        place_2 = line["place_2"]
        places.add(place_1)
        places.add(place_2)
        distances[_get_key(place_1, place_2)] = int(line["dist"])

    output_distance = None
    for route in permutations(places):
        distance = 0
        for place_1, place_2 in zip(route, route[1:]):
            distance += distances[_get_key(place_1, place_2)]
        output_distance = cmp_fn(output_distance, distance)
    return output_distance


def part1() -> int:
    return _get_distance(utils.safe_min)


def part2() -> int:
    return _get_distance(utils.safe_max)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
