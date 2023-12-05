from aoc import utils


def get_data():
    return [
        [int(i) for i in line.split("\t") if i] for line in utils.load_data(2017, 2)
    ]


def part1():
    total = 0
    data = get_data()
    for row in data:
        total += max(row) - min(row)
    return total


def get_row_quotient(row):
    for i, v1 in enumerate(row, start=1):
        for v2 in row[i:]:
            small, big = sorted((v1, v2), key=abs)
            q = big / small
            if q.is_integer():
                return int(q)
    raise Exception("Didn't find any divisible pairs")


def part2():
    total = 0
    data = get_data()
    for row in data:
        total += get_row_quotient(row)
    return total


if __name__ == "__main__":
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
