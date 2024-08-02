import argparse
import datetime
from importlib import import_module
from zoneinfo import ZoneInfo

from rich import print

from aoc import config, utils


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int, nargs="?")
    parser.add_argument(
        "-y",
        "--year",
        type=int,
        help="In December defaults to this year, otherwise last year",
    )
    parser.add_argument(
        "-e", "--example", action="store_true", help="Use example input"
    )
    parser.add_argument("-1", "--part-1", action="store_true")
    parser.add_argument("-2", "--part-2", action="store_true")

    parser.add_argument("-p", "--print-data", action="store_true")

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

    example = args.example
    config.EXAMPLE = example

    part_1 = args.part_1
    part_2 = args.part_2

    if not part_1 and not part_2:
        part_1 = part_2 = True

    module_name = f"aoc.aoc{year}.day{day:02d}"
    print(f"Loading {module_name}")

    try:
        day_module = import_module(module_name)
    except ModuleNotFoundError as e:
        print(e)
        return

    with utils.timed("Load data"):
        data_raw = utils.load_data_raw(year=year, day=day, example=example)

    if args.print_data:
        for line in data_raw:
            print(line)
        return

    try:
        parse_data = day_module.parse_data
    except AttributeError:
        print("parse_data not found; using raw data")
        data = data_raw
    else:
        with utils.timed("Parse data"):
            data = parse_data(data_raw)

    if part_1:
        with utils.timed():
            answer = day_module.part1(data=data)
            print()
            print(f"Part 1: {answer}")

    if part_2:
        with utils.timed():
            answer = day_module.part2(data=data)
            print()
            print(f"Part 2: {answer}")


if __name__ == "__main__":
    main()
