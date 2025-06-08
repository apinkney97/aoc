type Data = list[str]


def to_id(seat: str) -> int:
    binary = (
        seat.replace("B", "1").replace("F", "0").replace("L", "0").replace("R", "1")
    )
    return int(binary, 2)


def part1(data: Data) -> int:
    max_seat = 0
    for row in data:
        max_seat = max(max_seat, to_id(row))
    return max_seat


def part2(data: Data) -> int:
    all_seats = {to_id(row) for row in data}

    missing = set(range(max(all_seats) + 1)) - all_seats

    for seat in missing:
        if (seat - 1) in all_seats and (seat + 1) in all_seats:
            return seat

    raise Exception("No seat found")
