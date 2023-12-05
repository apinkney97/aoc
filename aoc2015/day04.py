from hashlib import md5
from itertools import count

import utils

DATA = utils.load_data(2015, 4)


def find_hash(leading_zeros):
    key = DATA[0]
    match = "0" * leading_zeros
    for i in count():
        if md5(f"{key}{i}".encode()).hexdigest().startswith(match):
            return i


def part1() -> int:
    return find_hash(5)


def part2() -> int:
    return find_hash(6)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
