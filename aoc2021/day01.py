import utils


def load_data():
    data = utils.load_data(1, fn=int)

    return data


DATA = load_data()


def part1() -> int:
    return count_increases(DATA)


def count_increases(data):
    increases = 0
    for i, j in zip(data, data[1:]):
        if j > i:
            increases += 1
    return increases


def part2() -> int:
    windows = [sum(x) for x in zip(DATA, DATA[1:], DATA[2:])]
    return count_increases(windows)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
