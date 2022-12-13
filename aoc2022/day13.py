import ast
import functools
import itertools

import more_itertools

import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(13, example=EXAMPLE)
    parsed = []
    for packet_1, packet_2, _ in more_itertools.grouper(
        data, 3, incomplete="fill", fillvalue=""
    ):
        packet_1 = ast.literal_eval(packet_1)
        packet_2 = ast.literal_eval(packet_2)
        parsed.append((packet_1, packet_2))
    return parsed


DATA = load_data()


def cmp(left, right):
    # both ints
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        if left > right:
            return 1
        return 0

    # one list
    if isinstance(left, int):
        return cmp([left], right)
    if isinstance(right, int):
        return cmp(left, [right])

    # both lists
    for sub_left, sub_right in itertools.zip_longest(left, right):
        if sub_left is None and sub_right is not None:
            return -1
        if sub_left is not None and sub_right is None:
            return 1
        result = cmp(sub_left, sub_right)
        if result != 0:
            return result

    return 0


def part1() -> int:
    total = 0
    for i, (left, right) in enumerate(DATA, start=1):
        result = cmp(left, right)
        if result == -1:
            total += i
    return total


def part2() -> int:
    all_packets = []
    for left, right in DATA:
        all_packets.extend([left, right])

    marker_1 = [[2]]
    marker_2 = [[6]]
    all_packets.append(marker_1)
    all_packets.append(marker_2)

    all_packets.sort(key=functools.cmp_to_key(cmp))

    return (all_packets.index(marker_1) + 1) * (all_packets.index(marker_2) + 1)


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
