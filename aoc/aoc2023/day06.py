from aoc import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(2023, 6, example=EXAMPLE)

    times = [int(n) for n in data[0].split(":")[1].split()]
    distances = [int(n) for n in data[1].split(":")[1].split()]
    return times, distances


with utils.timed("Load data"):
    DATA = load_data()


def part1() -> int:
    result = 1

    for time, record in zip(*DATA):
        wins = 0
        for speed in range(1, time):
            run_time = time - speed
            distance = run_time * speed
            if distance > record:
                wins += 1
        result *= wins

    return result


def part2() -> int:
    time, record = DATA
    time = int("".join(str(t) for t in time))
    record = int("".join(str(r) for r in record))
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

    return last_win - first_win + 1


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
