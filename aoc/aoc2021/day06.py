from collections import Counter

from aoc import utils


def load_data():
    data = utils.load_data(2021, 6, example=False)

    return [int(i) for i in data[0].split(",")]


DATA = load_data()


def step(fish: dict[int, int]) -> dict[int, int]:
    new_fish = {k - 1: v for k, v in fish.items()}
    expired = new_fish.pop(-1, 0)
    new_fish[8] = expired
    if 6 not in new_fish:
        new_fish[6] = 0
    new_fish[6] += expired
    return new_fish


def part1(steps=80) -> int:
    fish = Counter(DATA)
    for _ in range(steps):
        fish = step(fish)

    return sum(fish.values())


def part2() -> int:
    return part1(256)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
