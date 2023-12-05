from aoc import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(2022, 1, example=EXAMPLE)
    parsed = []
    current = []
    for row in data:
        if not row:
            parsed.append(current)
            current = []
        else:
            current.append(int(row))
    if current:
        parsed.append(current)
    return parsed


DATA = load_data()


def part1() -> int:
    return max(sum(elf) for elf in DATA)


def part2() -> int:
    return sum(sorted(sum(elf) for elf in DATA)[-3:])


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
