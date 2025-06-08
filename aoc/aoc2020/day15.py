type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(i) for i in data[0].split(",")]


def mem_game(data: Data, n: int) -> int:
    seen: dict[int, list[int]] = {}
    for i, d in enumerate(data):
        seen.setdefault(d, []).append(i)

    last = data[-1]
    for i in range(len(data), n):
        last_seen = seen.get(last, [])
        if len(last_seen) < 2:
            new_val = 0
        else:
            new_val = last_seen[-1] - last_seen[-2]
        last = new_val
        seen.setdefault(new_val, []).append(i)

    return last


def part1(data: Data) -> int:
    return mem_game(data, 2020)


def part2(data: Data) -> int:
    return mem_game(data, 30000000)
