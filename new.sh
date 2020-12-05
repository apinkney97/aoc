#!/bin/bash

set -euC

day_num=$1
day_str=$(printf 'day%02d' "${day_num}")
year=${2:-2020}

dirname="aoc${year}"

mkdir -p "${dirname}/data/"

touch "${dirname}/data/${day_str}.data"
cat > "${dirname}/${day_str}.py" <<EOF
import utils

DATA = utils.load_data(${day_num})


def part1() -> int:
    pass


def part2() -> int:
    pass


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
EOF
