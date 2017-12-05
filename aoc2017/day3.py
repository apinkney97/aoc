"""
    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

utilise fact that squares of odd numbers are at bottom right of spiral segment of that length
"""
from math import sqrt, ceil


def part1(n):
    if n == 1:
        return 0
    side_len = int(ceil(sqrt(n)))
    if side_len % 2 == 0:
        side_len += 1
    upper_bound = side_len ** 2
    lower_bound = (side_len - 2) ** 2
    layer = range(lower_bound + 1, upper_bound + 1)
    segment_len = side_len - 1
    for i in range(4):
        segment = layer[i*segment_len:i*segment_len + segment_len]
        if n in segment:
            break

    d1 = side_len // 2
    d2 = abs(segment[d1 - 1] - n)
    return d1 + d2


def part2(n):
    pass


if __name__ == '__main__':
    n = 368078
    print("Part 1: {}".format(part1(n)))
    print("Part 2: {}".format(part2(n)))
