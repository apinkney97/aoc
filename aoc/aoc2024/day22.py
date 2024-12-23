import collections


def parse_data(data):
    return [int(i) for i in data]


def get_next_num(num: int) -> int:
    num = ((num << 6) ^ num) & 16777215
    num = ((num >> 5) ^ num) & 16777215
    num = ((num << 11) ^ num) & 16777215
    return num


def get_next_nth(num, n):
    for _ in range(n):
        num = get_next_num(num)
    return num


def get_all_prices(start: int):
    num = start
    prev_4 = (None, None, None, None)

    price = start % 10
    # yield price, diff, prev_4

    for _ in range(2000):
        prev_price = price
        num = get_next_num(num)
        price = num % 10
        diff = price - prev_price
        prev_4 = prev_4[1:] + (diff,)
        if None not in prev_4:
            yield price, prev_4


def part1(data) -> int:
    result = 0
    for num in data:
        num = get_next_nth(num, 2000)
        result += num
    return result


def part2(data) -> int:
    counts = collections.Counter()

    for num in data:
        first = {}
        for price, diffs in get_all_prices(num):
            if diffs in first:
                continue
            first[diffs] = price

        for diffs, price in first.items():
            counts[diffs] += price

    return max(counts.values())
