from itertools import count

type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(line) for line in data]


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

    raise Exception("No solution found")


def part1(data: Data) -> int:
    loop_size = find_loop_size(data[0])
    return transform(data[1], loop_size)


def part2(data: Data) -> str:
    return "*"
