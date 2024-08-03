from aoc import utils


def parse_data(data):
    return utils.parse_data(data, fn=int)


def part1(data):
    data = data[:]
    index = 0
    count = 0
    while 0 <= index < len(data):
        val = data[index]
        data[index] += 1
        index += val
        count += 1
    return count


def part2(data):
    data = data[:]
    index = 0
    count = 0
    while 0 <= index < len(data):
        val = data[index]
        data[index] += 1 if val < 3 else -1
        index += val
        count += 1
    return count
