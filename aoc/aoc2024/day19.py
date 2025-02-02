import functools

from aoc import utils

TOWELS: set[str] = set()

type Data = list[str]


def parse_data(data: list[str]) -> Data:
    global TOWELS
    towels, patterns = utils.split_by_blank_lines(data)
    TOWELS = set(towels[0].split(", "))
    return patterns


@functools.cache
def string_match(pattern: str, start: int, end: int, towel: str) -> bool:
    return pattern[start:end] == towel


def match(pattern: str) -> bool:
    queue = [0]
    seen = set()
    while queue:
        offset = queue.pop()
        for towel in TOWELS:
            towel_len = len(towel)
            next_offset = offset + towel_len
            if next_offset in seen:
                continue
            if string_match(pattern, offset, next_offset, towel):
                queue.append(next_offset)
                seen.add(next_offset)
                if next_offset == len(pattern):
                    return True

    return False


@functools.cache
def match_all(pattern: str, offset: int) -> int:
    matches = 0
    for towel in TOWELS:
        towel_len = len(towel)
        next_offset = offset + towel_len
        if string_match(pattern, offset, next_offset, towel):
            if next_offset == len(pattern):
                matches += 1
            else:
                matches += match_all(pattern, next_offset)
    return matches


def part1(data: Data) -> int:
    patterns = data
    result = 0
    for pattern in patterns:
        if match(pattern):
            result += 1
    return result


def part2(data: Data) -> int:
    patterns = data
    result = 0
    for i, pattern in enumerate(patterns):
        count = match_all(pattern, 0)
        # print(i, count)
        result += count
    return result
