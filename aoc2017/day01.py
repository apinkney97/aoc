import utils


def get_data():
    return utils.load_data(2017, 1)[0]


def part1():
    data = get_data()
    total = 0
    for i, d in enumerate(data):
        if d == data[i - 1]:
            total += int(d)
    return total


def part2():
    data = get_data()
    total = 0
    half = len(data) // 2

    for i, d in enumerate(data):
        if d == data[(i + half) % len(data)]:
            total += int(d)

    return total


if __name__ == "__main__":
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
