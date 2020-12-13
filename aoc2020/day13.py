import utils


def _load_data():
    data = utils.load_data(13, example=False)
    return int(data[0]), [int(a if a != "x" else 0) for a in data[1].split(",")]


DATA = _load_data()


def part1() -> int:
    now, buses = DATA

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
    prod = utils.product(*remainders.keys())
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


def part2() -> int:
    remainders = {}
    for i, bus in enumerate(DATA[1]):
        if bus:
            remainder = (bus - i) % bus
            remainders[bus] = remainder

    return chinese_remainder(remainders)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
