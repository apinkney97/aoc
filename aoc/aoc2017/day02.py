def parse_data(data):
    return [[int(i) for i in line.split("\t") if i] for line in data]


def part1(data):
    total = 0
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


def part2(data):
    total = 0
    for row in data:
        total += get_row_quotient(row)
    return total
