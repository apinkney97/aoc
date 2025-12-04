from aoc.utils import log, neighbours

type Data = list[list[str]]


def parse_data(data: list[str]) -> Data:
    return [list(line) for line in data]


def part1(data: Data) -> int:
    result = 0
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell != "@":
                continue
            paper_count = 0
            for nx, ny in neighbours((x, y), include_diagonals=True):
                if nx < 0 or ny < 0 or nx >= len(row) or ny >= len(data):
                    continue
                if data[ny][nx] == "@":
                    paper_count += 1
            if paper_count < 4:
                result += 1

    return result


def part2(data: Data) -> int:
    for line in data:
        log("".join(line))
    log()

    result = 0
    changed = True
    while changed:
        changed = False
        for y, row in enumerate(data):
            for x, cell in enumerate(row):
                if cell != "@":
                    continue
                paper_count = 0
                for nx, ny in neighbours((x, y), include_diagonals=True):
                    if nx < 0 or ny < 0 or nx >= len(row) or ny >= len(data):
                        continue
                    if data[ny][nx] == "@":
                        paper_count += 1
                if paper_count < 4:
                    data[y][x] = "."
                    result += 1
                    changed = True

    for line in data:
        log("".join(line))
    return result
