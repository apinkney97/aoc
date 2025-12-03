type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(line) for line in data]


def part1(data: Data) -> int:
    data = data[:]
    index = 0
    count = 0
    while 0 <= index < len(data):
        val = data[index]
        data[index] += 1
        index += val
        count += 1
    return count


def part2(data: Data) -> int:
    data = data[:]
    index = 0
    count = 0
    while 0 <= index < len(data):
        val = data[index]
        data[index] += 1 if val < 3 else -1
        index += val
        count += 1
    return count
