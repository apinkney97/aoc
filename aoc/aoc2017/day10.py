from functools import reduce

from aoc import utils


def get_data():
    return utils.load_data(2017, 10)[0]


def circular_slice(sliceable, start, length):
    if length > len(sliceable):
        raise Exception("Slice length too long")

    vals = sliceable[start : start + length]
    if len(vals) < length:
        vals += sliceable[0 : length - len(vals)]
    return vals


def circular_overwrite(sliceable, start, values):
    end = min(len(sliceable), start + len(values))
    sliceable[start:end] = values[: end - start]

    if end == len(sliceable):
        sliceable[: len(values) + start - end] = values[end - start :]


def knot_hash_round(list_, lengths, pos=0, skip=0):
    for i in lengths:
        circular_overwrite(list_, pos, list(reversed(circular_slice(list_, pos, i))))
        pos = (pos + i + skip) % len(list_)
        skip += 1

    return pos, skip


def knot_hash(data):
    lengths = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    list_ = list(range(256))

    pos = 0
    skip = 0
    for _ in range(64):
        pos, skip = knot_hash_round(list_, lengths, pos, skip)

    ns = tuple(reduce(lambda x, y: x ^ y, list_[i : i + 16]) for i in range(0, 256, 16))
    return ("%02x" * 16) % ns


def part1():
    list_ = list(range(256))
    knot_hash_round(list_, (int(i) for i in get_data().split(",")))
    return list_[0] * list_[1]


def part2():
    return knot_hash(get_data())


if __name__ == "__main__":
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
