def part1(data) -> int:
    x = 0
    y = 0
    for line in data:
        match line.split():
            case ["forward", dist]:
                x += int(dist)
            case ["down", dist]:
                y += int(dist)
            case ["up", dist]:
                y -= int(dist)

    return x * y


def part2(data) -> int:
    aim = 0
    x = 0
    y = 0
    for line in data:
        match line.split():
            case ["forward", dist]:
                dist = int(dist)
                x += dist
                y += aim * dist
            case ["down", dist]:
                aim += int(dist)
            case ["up", dist]:
                aim -= int(dist)

    return x * y
