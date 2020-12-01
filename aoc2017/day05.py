from aoc2017.util import load_data


def get_data():
    return [int(line) for line in load_data(5)]


def part1():
    data = get_data()

    index = 0
    count = 0
    while 0 <= index < len(data):
        val = data[index]
        data[index] += 1
        index += val
        count += 1
    return count


def part2():
    data = get_data()

    index = 0
    count = 0
    while 0 <= index < len(data):
        val = data[index]
        data[index] += (1 if val < 3 else -1)
        index += val
        count += 1
    return count


if __name__ == '__main__':
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
