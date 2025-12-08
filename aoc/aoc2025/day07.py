type Data = list[list[str]]


def parse_data(data: list[str]) -> Data:
    return [list(line) for line in data]


def part1(data: Data) -> int:
    result = 0
    beams = {data[0].index("S")}
    for row in data[1:]:
        new_beams = set()
        for beam in beams:
            if row[beam] == "^":
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
                result += 1
            else:
                new_beams.add(beam)
        beams = new_beams
    return result


def part2(data: Data) -> int:
    reachableness = [[0] * len(data[1]) for _ in data]
    start = data[0].index("S")
    reachableness[0][start] = 1
    beams = {start}
    for i, row in enumerate(data[1:], start=1):
        new_beams = set()
        for beam in beams:
            parent = reachableness[i - 1][beam]
            if row[beam] == "^":
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
                reachableness[i][beam - 1] += parent
                reachableness[i][beam + 1] += parent
            else:
                reachableness[i][beam] += parent
                new_beams.add(beam)
        beams = new_beams

    return sum(reachableness[-1])
