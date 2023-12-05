import re

import utils

RE = re.compile(r"^(\d+)x(\d+)x(\d+)$")


def _get_data():
    data = utils.load_data(2015, 2, fn=RE.match)
    dimensions = [sorted(int(item[i]) for i in (1, 2, 3)) for item in data]
    return dimensions


DATA = _get_data()


def part1() -> int:
    total = 0
    for ds in DATA:
        total += 3 * ds[0] * ds[1]
        total += 2 * ds[0] * ds[2]
        total += 2 * ds[1] * ds[2]

    return total


def part2() -> int:
    total = 0
    for ds in DATA:
        total += 2 * (ds[0] + ds[1])
        total += utils.product(ds)

    return total


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
