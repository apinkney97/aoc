type Data = tuple[list[int], list[int]]


def parse_data(data: list[str]) -> Data:
    times = [int(n) for n in data[0].split(":")[1].split()]
    distances = [int(n) for n in data[1].split(":")[1].split()]
    return times, distances


def part1(data: Data) -> int:
    result = 1

    for time, record in zip(*data):
        wins = 0
        for speed in range(1, time):
            run_time = time - speed
            distance = run_time * speed
            if distance > record:
                wins += 1
        result *= wins

    return result


def part2(data: Data) -> int:
    times, records = data
    time = int("".join(str(t) for t in times))
    record = int("".join(str(r) for r in records))
    print(time, record)

    first_win = last_win = None

    for speed in range(1, time):
        run_time = time - speed
        distance = run_time * speed
        if distance > record:
            first_win = speed
            print(f"{first_win=}")
            break

    for speed in range(time, 1, -1):
        run_time = time - speed
        distance = run_time * speed
        if distance > record:
            last_win = speed
            print(f"{last_win=}")
            break

    assert last_win is not None and first_win is not None
    return last_win - first_win + 1
