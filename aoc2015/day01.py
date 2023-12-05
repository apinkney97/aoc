import utils

DATA = utils.load_data(2015, 1)


def part1() -> int:
    return DATA[0].count("(") - DATA[0].count(")")


def part2() -> int:
    floor = 0
    for i, char in enumerate(DATA[0]):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor < 0:
            return i + 1

    raise Exception("No solution found")


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
