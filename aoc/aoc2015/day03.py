def parse_data(data):
    return data[0]


def part1(data) -> int:
    x = 0
    y = 0
    visited = {(x, y)}

    for char in data:
        if char == "^":
            y += 1
        elif char == "v":
            y -= 1
        elif char == ">":
            x += 1
        elif char == "<":
            x -= 1
        else:
            raise Exception(f"Bad char {char}")

        visited.add((x, y))

    return len(visited)


def part2(data) -> int:
    x = [0, 0]
    y = [0, 0]
    visited = {(0, 0)}

    for i, char in enumerate(data):
        i = i % 2
        if char == "^":
            y[i] += 1
        elif char == "v":
            y[i] -= 1
        elif char == ">":
            x[i] += 1
        elif char == "<":
            x[i] -= 1
        else:
            raise Exception(f"Bad char {char}")

        visited.add((x[i], y[i]))

    return len(visited)
