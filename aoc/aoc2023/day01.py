import re


def part1(data) -> int:
    total = 0
    for line in data:
        line = re.sub(r"\D", "", line)
        total += 10 * int(line[0]) + int(line[-1])
    return total


def part2(data) -> int:
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    matcher = re.compile("|".join(numbers.keys()) + r"|\d")
    rev_matcher = re.compile("|".join(k[::-1] for k in numbers.keys()) + r"|\d")

    total = 0
    for line in data:
        match = matcher.search(line)
        assert match is not None
        first_digit = match.group(0)
        first_digit = numbers.get(first_digit, first_digit)

        line = line[::-1]

        match = rev_matcher.search(line)
        assert match is not None
        last_digit = match.group(0)[::-1]
        last_digit = numbers.get(last_digit, last_digit)

        total += 10 * int(first_digit) + int(last_digit)

    return total
