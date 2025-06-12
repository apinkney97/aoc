import re
from collections.abc import Generator
from itertools import count

type Data = tuple[int, int]


def sequence(start: int = 20151125) -> Generator[int, None, None]:
    val = start
    while True:
        yield val
        val = (val * 252533) % 33554393


def coords() -> Generator[tuple[int, int], None, None]:
    for coord_sum in count(start=2):
        for x in range(1, coord_sum):
            yield x, coord_sum - x


def parse_data(data: list[str]) -> Data:
    vals = []
    for match in re.findall(r"\d+", data[0]):
        vals.append(int(match))
    return vals[1], vals[0]


def part1(data: Data) -> int:
    result = 0
    for i, val in zip(coords(), sequence()):
        if i == data:
            return val
    return result


def part2(data: Data) -> int:
    result = 0
    return result
