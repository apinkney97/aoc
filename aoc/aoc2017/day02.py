type Data = list[list[int]]


def parse_data(data: list[str]) -> Data:
    return [[int(i) for i in line.split("\t") if i] for line in data]


def part1(data: Data) -> int:
    total = 0
    for row in data:
        total += max(row) - min(row)
    return total


def get_row_quotient(row: list[int]) -> int:
    for i, v1 in enumerate(row, start=1):
        for v2 in row[i:]:
            small, big = sorted((v1, v2), key=abs)
            q, r = divmod(big, small)
            if r == 0:
                return q
    raise Exception("Didn't find any divisible pairs")


def part2(data: Data) -> int:
    total = 0
    for row in data:
        total += get_row_quotient(row)
    return total
