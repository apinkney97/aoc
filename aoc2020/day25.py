from itertools import count

import utils


def load_data():
    data = utils.load_data(2020, 25, fn=int)

    return data


DATA = load_data()


def transform(subject: int, loop_size: int) -> int:
    value = 1
    for _ in range(loop_size):
        value = (value * subject) % 20201227
    return value


def find_loop_size(expected: int) -> int:
    value = 1
    for i in count():
        if value == expected:
            return i
        value = (value * 7) % 20201227


def part1() -> int:
    loop_size = find_loop_size(DATA[0])
    return transform(DATA[1], loop_size)


def main() -> None:
    print(f"Part 1: {part1()}")


if __name__ == "__main__":
    main()
