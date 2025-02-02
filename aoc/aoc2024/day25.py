from aoc import utils

type Data = tuple[list[list[int]], list[list[int]]]


def parse_data(data: list[str]) -> Data:
    keys = []
    locks = []
    for lines in utils.split_by_blank_lines(data):
        rotated = utils.rotate_clockwise(lines)
        if lines[0][0] == ".":
            key = []
            for line in rotated:
                key.append(line.index(".") - 1)
            keys.append(key)
        else:
            lock = []
            for line in rotated:
                lock.append(line[::-1].index(".") - 1)
            locks.append(lock)

    return locks, keys


def part1(data: Data) -> int:
    result = 0
    locks, keys = data
    for lock in locks:
        for key in keys:
            for l_height, k_height in zip(lock, key):
                if l_height + k_height > 5:
                    break
            else:
                result += 1
    return result


def part2(data: Data) -> str:
    return "*"
