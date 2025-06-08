from math import ceil, sqrt

type Data = int


def parse_data(data: list[str]) -> Data:
    return int(data[0])


def part1(data: Data) -> int:
    """
    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23---> ...

    utilise fact that squares of odd numbers are at bottom right of spiral segment of that length
    """
    num = data
    if num == 1:
        return 0
    side_len = int(ceil(sqrt(num)))
    if side_len % 2 == 0:
        side_len += 1
    upper_bound = side_len**2
    lower_bound = (side_len - 2) ** 2
    layer = range(lower_bound + 1, upper_bound + 1)
    segment_len = side_len - 1
    for i in range(4):
        segment = layer[i * segment_len : i * segment_len + segment_len]
        if num in segment:
            break

    d1 = side_len // 2
    d2 = abs(segment[d1 - 1] - num)
    return d1 + d2


def part2(data: Data) -> int:
    """
    Neighbours:

    1:                                                           (special case)
    2:  1                                                        (special case)
    3:  1 2                                                      (special case)
    4:  1 2 3                                                    (special case)
    5:  1     4                                                  (special case)
    6:  1     4 5                                                (special case)
    7:  1         6                                              corner
    8:  1 2       6 7                                            after
    9:  1 2           8                                          before
    10:   2             9                                        corner
    11:   2 3           9 10                                     after
    12:   2 3                11                                  before
    13:     3                   12                               corner
    14:     3 4                 12 13                            after
    15:     3 4 5                     14                         edge
    16:       4 5                        15                      before
    17:         5                           16                   corner
    18:         5 6                         16 17                after
    19:         5 6 7                             18             edge
    20:           6 7                                19          before
    21:             7                                   20       corner
    22:             7 8                                 20 21    after
    23:             7 8 9                                     22 edge
    24:               8 9 10                                     edge
    25:                 9 10                                     before

    The square before a corner has 3 (2 lower and immediate predecessor)
    Corner squares have 2 (1 lower and immediate predecessor)
    The square after a corner has 4 (2 lower and 2 immediate predecessors)
    Other edge squares have 4 (3 lower and immediate predecessor)
    """
    target = data

    sl = 1.0
    n = 1

    vals = {
        1: 1,
        2: 1,
        3: 2,
        4: 4,
        5: 5,
        6: 10,
    }

    inner = 0

    while True:
        actual_side_length = int(sl)
        side = list(range(n, n + actual_side_length))
        # print(side)

        for i, num in enumerate(side):
            if num in vals:
                continue

            if i not in (1, 2):
                # increment value on inner spiral except on 2 squares after a corner
                inner += 1

            indices = {inner, num - 1}

            if i == 0:  # corner
                pass
            elif i == 1:  # after
                indices.add(num - 2)
                indices.add(inner + 1)
            elif i == actual_side_length - 1:  # before
                indices.add(inner + 1)
            else:  # edge
                indices.add(inner + 1)
                indices.add(inner + 2)

            total = 0
            for index in indices:
                total += vals[index]

            if total > target:
                return total

            vals[num] = total

        n += actual_side_length
        sl += 0.5
