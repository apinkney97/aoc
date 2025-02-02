from hashlib import md5
from itertools import count

type Data = str


def parse_data(data: list[str]) -> Data:
    return data[0]


def find_hash(key: str, leading_zeros: int) -> int:
    match = "0" * leading_zeros
    for i in count():
        if md5(f"{key}{i}".encode()).hexdigest().startswith(match):
            return i

    raise Exception("No hash found")


def part1(data: Data) -> int:
    return find_hash(data, 5)


def part2(data: Data) -> int:
    return find_hash(data, 6)
