import re


def part1(data: list[str]) -> int:
    matcher = re.compile(r"mul\((\d+),(\d+)\)")
    result = 0
    for line in data:
        for match in matcher.findall(line):
            result += int(match[0]) * int(match[1])
    return result


def part2(data: list[str]) -> int:
    matcher = re.compile(
        r"""
            (mul) \( (\d+) , (\d+) \)
            |
            (do) \(\)
            |
            (don't) \(\)
        """,
        re.VERBOSE,
    )
    result = 0
    do = True
    for line in data:
        for match in matcher.findall(line):
            if match[3] == "do":
                do = True
            elif match[4] == "don't":
                do = False
            elif do and match[0] == "mul":
                result += int(match[1]) * int(match[2])
    return result
