def parse_data(data):
    return data[0]


def part1(data) -> int:
    return data.count("(") - data.count(")")


def part2(data) -> int:
    floor = 0
    for i, char in enumerate(data):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor < 0:
            return i + 1

    raise Exception("No solution found")
