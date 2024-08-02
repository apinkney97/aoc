from collections import Counter


def parse_data(data):
    return [int(i) for i in data[0].split(",")]


def step(fish: dict[int, int]) -> dict[int, int]:
    new_fish = {k - 1: v for k, v in fish.items()}
    expired = new_fish.pop(-1, 0)
    new_fish[8] = expired
    if 6 not in new_fish:
        new_fish[6] = 0
    new_fish[6] += expired
    return new_fish


def part1(data, steps=80) -> int:
    fish = Counter(data)
    for _ in range(steps):
        fish = step(fish)

    return sum(fish.values())


def part2(data) -> int:
    return part1(data, 256)
