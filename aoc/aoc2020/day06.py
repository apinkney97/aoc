from aoc import utils

DATA = utils.load_data(2020, 6)


def part1() -> int:
    total = 0
    group = set()
    for line in DATA:
        if not line:
            total += len(group)
            group = set()
        else:
            group |= set(line)

    total += len(group)

    return total


def part2() -> int:
    total = 0
    group = None
    for line in DATA:
        if not line:
            total += len(group)
            group = None
        else:
            if group is None:
                group = set(line)
            else:
                group &= set(line)
    total += len(group)

    return total


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
