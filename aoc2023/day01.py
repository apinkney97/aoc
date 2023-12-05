import re

import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(2023, 1, example=EXAMPLE)

    return data


DATA = load_data()


def part1() -> int:
    total = 0
    for line in DATA:
        line = re.sub(r"\D", "", line)
        total += 10 * int(line[0]) + int(line[-1])
    return total


def part2() -> int:
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
    for line in DATA:
        first_digit = matcher.search(line).group(0)
        first_digit = numbers.get(first_digit, first_digit)

        line = line[::-1]

        last_digit = rev_matcher.search(line).group(0)[::-1]
        last_digit = numbers.get(last_digit, last_digit)

        total += 10 * int(first_digit) + int(last_digit)

    return total


def main() -> None:
    # with utils.timed():
    #     print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
