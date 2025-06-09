from __future__ import annotations

import ast
import functools
import itertools

import more_itertools

type Data = list[int | Data]


def parse_data(data: list[str]) -> Data:
    parsed = []
    for line in data:
        if line:
            parsed.append(ast.literal_eval(line))
    return parsed


def cmp(left: int | Data, right: int | Data) -> int:
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


def part1(data: Data) -> int:
    total = 0
    for i, (left, right) in enumerate(more_itertools.chunked(data, 2), start=1):
        result = cmp(left, right)
        if result == -1:
            total += i
    return total


def part2(data: Data) -> int:
    marker_1: Data = [[2]]
    marker_2: Data = [[6]]

    ordered = sorted(data + [marker_1, marker_2], key=functools.cmp_to_key(cmp))

    return (ordered.index(marker_1) + 1) * (ordered.index(marker_2) + 1)
