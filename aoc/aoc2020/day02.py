import re
import typing
from operator import xor


class Password(typing.NamedTuple):
    lower: int
    upper: int
    letter: str
    password: str


type Data = list[Password]


def parse_data(data: list[str]) -> Data:
    matcher = re.compile(
        r"^(?P<lower>\d+)-(?P<upper>\d+) (?P<letter>.): (?P<password>.*)$"
    )

    passwords = []

    for line in data:
        match = matcher.match(line)
        assert match is not None
        passwords.append(
            Password(
                lower=int(match["lower"]),
                upper=int(match["upper"]),
                letter=match["letter"],
                password=match["password"],
            )
        )

    return passwords


def part1(data: Data) -> int:
    valid = 0
    for pwd in data:
        if pwd.lower <= pwd.password.count(pwd.letter) <= pwd.upper:
            valid += 1
    return valid


def part2(data: Data) -> int:
    valid = 0
    for pwd in data:
        if xor(
            pwd.password[pwd.lower - 1] == pwd.letter,
            pwd.password[pwd.upper - 1] == pwd.letter,
        ):
            valid += 1
    return valid
