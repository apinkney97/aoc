import fractions
import re

from aoc import utils
from aoc.utils.coords import Coord, Vector

A_COST = 3
B_COST = 1


def parse_data(data):
    parsed = []

    for button_a, button_b, prize in utils.split_by_blank_lines(data):
        match = re.findall(r"\d+", button_a)
        a = Vector(int(match[0]), int(match[1]))

        match = re.findall(r"\d+", button_b)
        b = Vector(int(match[0]), int(match[1]))

        match = re.findall(r"\d+", prize)
        p = Coord(int(match[0]), int(match[1]))

        parsed.append((a, b, p))

    return parsed


def part1(data, extra=0) -> int:
    result = 0

    for a, b, prize in data:
        prize = prize + Vector(extra, extra)

        m_a = fractions.Fraction(a.y, a.x)
        m_b = fractions.Fraction(b.y, b.x)

        x = (prize.y - m_b * prize.x) / (m_a - m_b)

        if x % a.x == 0 and (prize.x - x) % b.x == 0:
            result += A_COST * x // a.x
            result += B_COST * (prize.x - x) // b.x

    return result


def part2(data) -> int:
    return part1(data, 10000000000000)