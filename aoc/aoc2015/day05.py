import re

from aoc import utils

DATA = utils.load_data(2015, 5)


PAIR_RE = re.compile(r"(.)(\1)")
VOWEL_RE = re.compile(r"[aeiou].*[aeiou].*[aeiou]")
BAD_STRINGS_RE = re.compile(r"ab|cd|pq|xy")

REPEATED_PAIR_RE = re.compile(r"(..).*(\1)")
REPEATED_ALTERNATING_LETTER_RE = re.compile(r"(.).(\1)")


def part1() -> int:
    nice = 0
    for string in DATA:
        if not PAIR_RE.search(string):
            print(f"{string} has no pair")
            continue
        if not VOWEL_RE.search(string):
            print(f"{string} has insufficient vowels")
            continue
        if BAD_STRINGS_RE.search(string):
            print(f"{string} has bad strings")
            continue
        nice += 1
    return nice


def part2() -> int:
    nice = 0
    for string in DATA:
        if not REPEATED_PAIR_RE.search(string):
            print(f"{string} has no repeated pair")
            continue
        if not REPEATED_ALTERNATING_LETTER_RE.search(string):
            print(f"{string} has no repeated alternating letter")
            continue
        nice += 1
    return nice


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
