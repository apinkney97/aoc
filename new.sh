#!/bin/bash

set -euC

day_num=${1:-$(date +'%-d')}
day_str=$(printf 'day%02d' "${day_num}")
year=${2:-$(date +'%Y')}

dirname="aoc${year}"

mkdir -p "${dirname}/data/"

touch "${dirname}/data/${day_str}.data"
touch "${dirname}/data/${day_str}-example.data"
cat > "${dirname}/${day_str}.py" <<EOF
import utils


EXAMPLE = True
# EXAMPLE = False


def load_data():
    data = utils.load_data(${day_num}, example=EXAMPLE)

    return data


DATA = load_data()


def part1() -> int:
    return 0


def part2() -> int:
    return 0


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
EOF
