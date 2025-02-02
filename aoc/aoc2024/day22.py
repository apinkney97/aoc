from collections import Counter
from typing import Generator

type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(i) for i in data]


def get_next_num(num: int) -> int:
    num = ((num << 6) ^ num) & 16777215
    num = ((num >> 5) ^ num) & 16777215
    num = ((num << 11) ^ num) & 16777215
    return num


def get_next_nth(num: int, n: int) -> int:
    for _ in range(n):
        num = get_next_num(num)
    return num


def get_all_prices(start: int) -> Generator[tuple[int, tuple[int, ...]]]:
    num = start
    diffs: list[int] = []

    price = start % 10
    # yield price, diff, prev_4

    for i in range(2000):
        prev_price = price
        num = get_next_num(num)
        price = num % 10
        diffs.append(price - prev_price)
        if i >= 3:
            yield price, tuple(diffs[-4:])


def part1(data: Data) -> int:
    result = 0
    for num in data:
        num = get_next_nth(num, 2000)
        result += num
    return result


def part2(data: Data) -> int:
    counts: Counter[tuple[int, ...]] = Counter()

    for num in data:
        first = {}
        for price, diffs in get_all_prices(num):
            if diffs in first:
                continue
            first[diffs] = price

        for diffs, price in first.items():
            counts[diffs] += price

    return max(counts.values())
