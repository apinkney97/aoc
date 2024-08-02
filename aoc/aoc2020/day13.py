from aoc import utils


def parse_data(data):
    return int(data[0]), [int(a if a != "x" else 0) for a in data[1].split(",")]


def part1(data) -> int:
    now, buses = data

    results = {}

    for bus in buses:
        if not bus:
            continue

        d, m = divmod(now, bus)
        next_time = (d + 1 if m else 0) * bus
        wait = next_time - now
        results[wait] = wait * bus

    return results[min(results)]


# shamelessly borrowed from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(remainders):
    total = 0
    prod = utils.product(remainders.keys())
    for bus, remainder in remainders.items():
        p = prod // bus
        total += remainder * mul_inv(p, bus) * p
    return total % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def part2(data) -> int:
    remainders = {}
    for i, bus in enumerate(data[1]):
        if bus:
            remainder = (bus - i) % bus
            remainders[bus] = remainder

    return chinese_remainder(remainders)
