from collections import Counter
from typing import Mapping

type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(i) for i in data[0].split(",")]


def step(fish: Mapping[int, int]) -> dict[int, int]:
    new_fish = {k - 1: v for k, v in fish.items()}
    expired = new_fish.pop(-1, 0)
    new_fish[8] = expired
    if 6 not in new_fish:
        new_fish[6] = 0
    new_fish[6] += expired
    return new_fish


def part1(data: Data, steps: int = 80) -> int:
    fish: Mapping[int, int] = Counter(data)
    for _ in range(steps):
        fish = step(fish)

    return sum(fish.values())


def part2(data: Data) -> int:
    return part1(data, 256)
