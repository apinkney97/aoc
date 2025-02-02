import re
from itertools import permutations

from aoc import utils
from aoc.utils.cmp import CmpFn

RE = re.compile(r"(?P<place_1>\w+) to (?P<place_2>\w+) = (?P<dist>\d+)")


type Data = list[re.Match[str]]


def parse_data(data: list[str]) -> Data:
    return [
        match for match in utils.parse_data(data, fn=RE.fullmatch) if match is not None
    ]


def _get_key(place_1: str, place_2: str) -> tuple[str, ...]:
    return tuple(sorted([place_1, place_2]))


def _get_distance(data: Data, cmp_fn: CmpFn) -> int:
    distances: dict[tuple[str, ...], int] = {}
    places = set()
    for line in data:
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
    assert isinstance(output_distance, int)
    return output_distance


def part1(data: Data) -> int:
    return _get_distance(data, utils.safe_min)


def part2(data: Data) -> int:
    return _get_distance(data, utils.safe_max)
