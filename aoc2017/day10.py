from functools import reduce

DATA = "70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41"


def circular_slice(l, start, length):
    if length > len(l):
        raise Exception("Slice length too long")

    vals = l[start:start + length]
    if len(vals) < length:
        vals += l[0:length - len(vals)]
    return vals


def circular_overwrite(l, start, values):
    end = min(len(l), start + len(values))
    l[start:end] = values[:end - start]

    if end == len(l):
        l[:len(values) + start - end] = values[end - start:]


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

    ns = tuple(reduce(lambda x, y: x ^ y, list_[i:i + 16]) for i in range(0, 256, 16))
    return ("%02x" * 16) % ns


def part1():
    list_ = list(range(256))
    knot_hash_round(list_, (int(i) for i in DATA.split(',')))
    return list_[0] * list_[1]


def part2():
    return knot_hash(DATA)


if __name__ == '__main__':
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
