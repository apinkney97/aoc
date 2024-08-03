def parse_data(data):
    return int(data[0])


def part1(data) -> int:
    for i in range(1, 100000):
        presents = 0
        for j in range(1, i + 1):
            if i % j == 0:
                presents += j
        presents *= 10
        if presents >= data:
            return i
    return 0


def part2(data) -> int:
    return 0
