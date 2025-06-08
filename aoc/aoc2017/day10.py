from functools import reduce
from typing import Iterable

type Data = str


def parse_data(data: list[str]) -> Data:
    return data[0]


def circular_slice(sliceable: list[int], start: int, length: int) -> list[int]:
    if length > len(sliceable):
        raise Exception("Slice length too long")

    vals = sliceable[start : start + length]
    if len(vals) < length:
        vals += sliceable[0 : length - len(vals)]
    return vals


def circular_overwrite(sliceable: list[int], start: int, values: list[int]) -> None:
    end = min(len(sliceable), start + len(values))
    sliceable[start:end] = values[: end - start]

    if end == len(sliceable):
        sliceable[: len(values) + start - end] = values[end - start :]


def knot_hash_round(
    list_: list[int], lengths: Iterable[int], pos: int = 0, skip: int = 0
) -> tuple[int, int]:
    for i in lengths:
        circular_overwrite(list_, pos, list(reversed(circular_slice(list_, pos, i))))
        pos = (pos + i + skip) % len(list_)
        skip += 1

    return pos, skip


def knot_hash(data: Data) -> str:
    lengths = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    list_ = list(range(256))

    pos = 0
    skip = 0
    for _ in range(64):
        pos, skip = knot_hash_round(list_, lengths, pos, skip)

    ns = tuple(reduce(lambda x, y: x ^ y, list_[i : i + 16]) for i in range(0, 256, 16))
    return ("%02x" * 16) % ns


def part1(data: Data) -> int:
    list_ = list(range(256))
    knot_hash_round(list_, (int(i) for i in data.split(",")))
    return list_[0] * list_[1]


def part2(data: Data) -> str:
    return knot_hash(data)
