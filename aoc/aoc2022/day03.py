import string

import more_itertools

SCORES = {
    letter: score
    for score, letter in enumerate(
        string.ascii_lowercase + string.ascii_uppercase, start=1
    )
}


def part1(data) -> int:
    total = 0
    for line in data:
        half = len(line) // 2
        common = (set(line[:half]) & set(line[half:])).pop()
        total += SCORES[common]
    return total


def part2(data) -> int:
    total = 0
    for elves in more_itertools.chunked(data, 3):
        common = (set(elves[0]) & set(elves[1]) & set(elves[2])).pop()
        total += SCORES[common]
    return total
