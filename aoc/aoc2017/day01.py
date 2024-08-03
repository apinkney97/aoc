def parse_data(data):
    return data[0]


def part1(data):
    total = 0
    for i, d in enumerate(data):
        if d == data[i - 1]:
            total += int(d)
    return total


def part2(data):
    total = 0
    half = len(data) // 2

    for i, d in enumerate(data):
        if d == data[(i + half) % len(data)]:
            total += int(d)

    return total
