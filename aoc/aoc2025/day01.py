type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [(-1 if line[0] == "L" else 1) * int(line[1:]) for line in data]


def part1(data: Data) -> int:
    result = 0
    dial = 50
    for num in data:
        dial = (dial + num) % 100
        if dial == 0:
            result += 1

    return result


def part2(data: Data) -> int:
    result = 0

    dial = 50
    for num in data:
        inc = num // abs(num)
        for _ in range(abs(num)):
            dial = (dial + inc) % 100
            if dial == 0:
                result += 1

    return result
