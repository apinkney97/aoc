import utils

DATA = utils.load_data(5)


def to_id(seat: str) -> int:
    binary = (
        seat.replace("B", "1").replace("F", "0").replace("L", "0").replace("R", "1")
    )
    return int(binary, 2)


def part1() -> int:
    max_seat = 0
    for row in DATA:
        max_seat = max(max_seat, to_id(row))
    return max_seat


def part2() -> int:
    all_seats = {to_id(row) for row in DATA}

    missing = set(range(max(all_seats) + 1)) - all_seats

    for seat in missing:
        if (seat - 1) in all_seats and (seat + 1) in all_seats:
            return seat

    raise Exception("No seat found")


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
