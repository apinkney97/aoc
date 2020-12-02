import re
from operator import xor

import utils

DATA = utils.load_data(2)

LINE_RE = re.compile(r"^(?P<lower>\d+)-(?P<upper>\d+) (?P<letter>.): (?P<password>.*)$")


def part1() -> int:
    valid = 0
    for line in DATA:
        match = LINE_RE.match(line)
        lower = int(match["lower"])
        upper = int(match["upper"])
        letter = match["letter"]
        password = match["password"]
        if lower <= password.count(letter) <= upper:
            valid += 1
    return valid


def part2() -> int:
    valid = 0
    for line in DATA:
        match = LINE_RE.match(line)
        pos_1 = int(match["lower"]) - 1
        pos_2 = int(match["upper"]) - 1
        letter = match["letter"]
        password = match["password"]
        if xor(password[pos_1] == letter, password[pos_2] == letter):
            valid += 1
    return valid


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
