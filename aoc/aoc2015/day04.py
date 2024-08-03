from hashlib import md5
from itertools import count


def parse_data(data):
    return data[0]


def find_hash(key, leading_zeros):
    match = "0" * leading_zeros
    for i in count():
        if md5(f"{key}{i}".encode()).hexdigest().startswith(match):
            return i


def part1(data) -> int:
    return find_hash(data, 5)


def part2(data) -> int:
    return find_hash(data, 6)
