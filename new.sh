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
def parse_data(data):
    return data


def part1(data) -> int:
    result = 0
    return result


def part2(data) -> int:
    result = 0
    return result
EOF
