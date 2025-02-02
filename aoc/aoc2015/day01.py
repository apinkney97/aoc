type Data = str


def parse_data(data: list[str]) -> Data:
    return data[0]


def part1(data: Data) -> int:
    return data.count("(") - data.count(")")


def part2(data: Data) -> int:
    floor = 0
    for i, char in enumerate(data):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor < 0:
            return i + 1

    raise Exception("No solution found")
