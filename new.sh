#!/bin/bash

set -euC

day_num=${1:-$(date +'%-d')}
day_str=$(printf 'day%02d' "${day_num}")
year=${2:-$(date +'%Y')}

dirname="aoc/aoc${year}"

mkdir -p "${dirname}/data/"

touch "${dirname}/data/${day_str}.data"
touch "${dirname}/data/${day_str}-example.data"
cat > "${dirname}/${day_str}.py" <<EOF
from aoc import utils


EXAMPLE = True
# EXAMPLE = False


def load_data():
    data = utils.load_data(${year}, ${day_num}, example=EXAMPLE)

    return data


with utils.timed("Load data"):
    DATA = load_data()


def part1() -> int:
    result = 0

    return result


def part2() -> int:
    result = 0

    return result


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
EOF
