import re

from aoc import utils

type Data = list[str]

PAIR_RE = re.compile(r"(.)(\1)")
VOWEL_RE = re.compile(r"[aeiou].*[aeiou].*[aeiou]")
BAD_STRINGS_RE = re.compile(r"ab|cd|pq|xy")

REPEATED_PAIR_RE = re.compile(r"(..).*(\1)")
REPEATED_ALTERNATING_LETTER_RE = re.compile(r"(.).(\1)")


def part1(data: Data) -> int:
    nice = 0
    for string in data:
        if not PAIR_RE.search(string):
            utils.log(f"{string} has no pair")
            continue
        if not VOWEL_RE.search(string):
            utils.log(f"{string} has insufficient vowels")
            continue
        if BAD_STRINGS_RE.search(string):
            utils.log(f"{string} has bad strings")
            continue
        nice += 1
    return nice


def part2(data: Data) -> int:
    nice = 0
    for string in data:
        if not REPEATED_PAIR_RE.search(string):
            utils.log(f"{string} has no repeated pair")
            continue
        if not REPEATED_ALTERNATING_LETTER_RE.search(string):
            utils.log(f"{string} has no repeated alternating letter")
            continue
        nice += 1
    return nice
