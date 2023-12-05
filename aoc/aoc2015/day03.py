from aoc import utils

DATA = utils.load_data(2015, 3)


def part1() -> int:
    x = 0
    y = 0
    visited = {(x, y)}

    for char in DATA[0]:
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


def part2() -> int:
    x = [0, 0]
    y = [0, 0]
    visited = {(0, 0)}

    for i, char in enumerate(DATA[0]):
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


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
