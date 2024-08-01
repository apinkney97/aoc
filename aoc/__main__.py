import argparse
import datetime
from importlib import import_module
from zoneinfo import ZoneInfo

from aoc import utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, nargs="?")
    parser.add_argument("year", type=int, nargs="?")
    parser.add_argument(
        "-e", "--example", action="store_true", help="Use example input"
    )
    parser.add_argument("-1", "--part-1", action="store_true")
    parser.add_argument("-2", "--part-2", action="store_true")

    args = parser.parse_args()

    day = args.day
    year = args.year

    # AoC runs on US Eastern time
    now = datetime.datetime.now(tz=ZoneInfo("America/New_York"))
    if now.month == 12:
        if day <= 25:
            day = day or now.day
        year = year or now.year
    else:
        year = year or now.year - 1

    if day is None or year is None:
        raise ValueError(
            f"You must specify a day and year (got day:{day}, year:{year})"
        )

    module_name = f"aoc.aoc{year}.day{day:02d}"
    print(f"Loading {module_name}")

    day_module = import_module(module_name)

    part_1 = args.part_1
    part_2 = args.part_2

    if not part_1 and not part_2:
        part_1 = part_2 = True

    if part_1:
        with utils.timed():
            print(f"Part 1: {day_module.part1()}")

    if part_2:
        with utils.timed():
            print(f"Part 2: {day_module.part2()}")


if __name__ == "__main__":
    main()
