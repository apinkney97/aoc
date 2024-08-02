import re
from operator import xor

from aoc import utils


def parse_data(data):
    matcher = re.compile(
        r"^(?P<lower>\d+)-(?P<upper>\d+) (?P<letter>.): (?P<password>.*)$"
    )

    return utils.parse_data(data, fn=matcher.match)


def part1(data) -> int:
    valid = 0
    for match in data:
        lower = int(match["lower"])
        upper = int(match["upper"])
        letter = match["letter"]
        password = match["password"]
        if lower <= password.count(letter) <= upper:
            valid += 1
    return valid


def part2(data) -> int:
    valid = 0
    for match in data:
        pos_1 = int(match["lower"]) - 1
        pos_2 = int(match["upper"]) - 1
        letter = match["letter"]
        password = match["password"]
        if xor(password[pos_1] == letter, password[pos_2] == letter):
            valid += 1
    return valid
