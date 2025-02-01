#!/bin/bash

set -euC

default_day=$(date +'%-d')
default_year=$(date +'%Y')

read -r -p "Enter year (${default_year}): " year
read -r -p "Enter day (${default_day}): " day

day=${day:-${default_day}}
year=${year:-${default_year}}

dir_name="aoc/aoc${year}"

mkdir -p "${dir_name}"
touch "${dir_name}/__init__.py"

module_name=$(printf 'day%02d' "${day}")

cat > "${dir_name}/${module_name}.py" <<EOF
def parse_data(data):
    return data


def part1(data) -> int:
    result = 0
    return result


def part2(data) -> int:
    result = 0
    return result
EOF
