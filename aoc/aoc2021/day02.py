from aoc import utils


def load_data():
    data = utils.load_data(2021, 2, example=False)

    return data


DATA = load_data()


def part1() -> int:
    x = 0
    y = 0
    for line in DATA:
        match line.split():
            case ["forward", dist]:
                x += int(dist)
            case ["down", dist]:
                y += int(dist)
            case ["up", dist]:
                y -= int(dist)

    return x * y


def part2() -> int:
    aim = 0
    x = 0
    y = 0
    for line in DATA:
        match line.split():
            case ["forward", dist]:
                dist = int(dist)
                x += dist
                y += aim * dist
            case ["down", dist]:
                aim += int(dist)
            case ["up", dist]:
                aim -= int(dist)

    return x * y


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
