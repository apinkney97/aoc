def part1(data) -> int:
    h = len(data)
    w = len(data[0])
    visible = 2 * w + 2 * h - 4

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            tree = data[y][x]

            # up
            for y1 in range(y - 1, -1, -1):
                if data[y1][x] >= tree:
                    break
            else:
                visible += 1
                continue

            # down
            for y1 in range(y + 1, h):
                if data[y1][x] >= tree:
                    break
            else:
                visible += 1
                continue

            # left
            for x1 in range(x - 1, -1, -1):
                if data[y][x1] >= tree:
                    break
            else:
                visible += 1
                continue

            # right
            for x1 in range(x + 1, w):
                if data[y][x1] >= tree:
                    break
            else:
                visible += 1
                continue

    return visible


def part2(data) -> int:
    h = len(data)
    w = len(data[0])

    score = 0

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            tree = data[y][x]

            up = 0
            for y1 in range(y - 1, -1, -1):
                up += 1
                if data[y1][x] >= tree:
                    break

            down = 0
            for y1 in range(y + 1, h):
                down += 1
                if data[y1][x] >= tree:
                    break

            left = 0
            for x1 in range(x - 1, -1, -1):
                left += 1
                if data[y][x1] >= tree:
                    break

            right = 0
            for x1 in range(x + 1, w):
                right += 1
                if data[y][x1] >= tree:
                    break

            score = max(score, up * down * left * right)

    return score
