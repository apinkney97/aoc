import utils


# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(8, example=EXAMPLE)
    return data


DATA = load_data()


def part1() -> int:
    h = len(DATA)
    w = len(DATA[0])
    visible = 2 * w + 2 * h - 4

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            tree = DATA[y][x]

            # up
            for y1 in range(y - 1, -1, -1):
                if DATA[y1][x] >= tree:
                    break
            else:
                visible += 1
                continue

            # down
            for y1 in range(y + 1, h):
                if DATA[y1][x] >= tree:
                    break
            else:
                visible += 1
                continue

            # left
            for x1 in range(x - 1, -1, -1):
                if DATA[y][x1] >= tree:
                    break
            else:
                visible += 1
                continue

            # right
            for x1 in range(x + 1, w):
                if DATA[y][x1] >= tree:
                    break
            else:
                visible += 1
                continue

    return visible


def part2() -> int:
    h = len(DATA)
    w = len(DATA[0])

    score = 0

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            tree = DATA[y][x]

            up = 0
            for y1 in range(y - 1, -1, -1):
                up += 1
                if DATA[y1][x] >= tree:
                    break

            down = 0
            for y1 in range(y + 1, h):
                down += 1
                if DATA[y1][x] >= tree:
                    break

            left = 0
            for x1 in range(x - 1, -1, -1):
                left += 1
                if DATA[y][x1] >= tree:
                    break

            right = 0
            for x1 in range(x + 1, w):
                right += 1
                if DATA[y][x1] >= tree:
                    break

            score = max(score, up * down * left * right)

    return score


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
