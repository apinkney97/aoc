from itertools import count
from typing import Generator

type Data = list[tuple[int, int]]


def parse_data(data: list[str]) -> Data:
    parsed = []
    for part in data[0].split(","):
        start, end = part.split("-")
        parsed.append((int(start), int(end)))
    return parsed


def get_start(value: int) -> int:
    value_str = str(value)
    midpoint = len(value_str) // 2
    start = value_str[:midpoint]
    return int(start or 1)


def bad_ids(range_start: int, range_end: int) -> Generator[int, None, None]:
    for half in count(start=get_start(range_start)):
        potential_id = int(f"{half}{half}")
        if potential_id < range_start:
            continue
        if potential_id > range_end:
            break
        yield potential_id


def part1(data: Data) -> int:
    result = 0
    for start, end in data:
        result += sum(bad_ids(start, end))
    return result


def bad_ids_2(range_start: int, range_end: int) -> Generator[int, None, None]:
    seen = set()
    for i in count(start=1):
        part = str(i)
        if int(part * 2) > range_end:
            break
        for n in count(start=2):
            potential_id = int(part * n)
            # print(f"{potential_id=}")

            if potential_id < range_start:
                continue
            if potential_id > range_end:
                break
            if potential_id not in seen:
                seen.add(potential_id)
                yield potential_id


def part2(data: Data) -> int:
    result = 0
    for start, end in data:
        result += sum(bad_ids_2(start, end))

    return result
