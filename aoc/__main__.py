import argparse
import datetime
import pkgutil
from importlib import import_module
from zoneinfo import ZoneInfo

from mypy.checker import NamedTuple
from rich.console import Console

from aoc import config, utils

CONSOLE = Console()


class RunConfig(NamedTuple):
    year: int
    day: int
    part_1: bool
    part_2: bool
    print_input: bool


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
    parser.add_argument("-1", "--part-1", action="store_true", help="Run part 1 only")
    parser.add_argument("-2", "--part-2", action="store_true", help="Run part 2 only")

    parser.add_argument(
        "-p", "--print-input", action="store_true", help="Print input to console"
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Enable debug output"
    )

    args = parser.parse_args()

    day = args.day
    year = args.year

    # AoC runs on US Eastern time
    now = datetime.datetime.now(tz=ZoneInfo("America/New_York"))
    if now.month == 12:
        if now.day <= 25:
            day = now.day if day is None else day
        year = now.year if year is None else year
    else:
        year = now.year - 1 if year is None else year

    if day is None or year is None:
        raise ValueError(
            f"You must specify a day and year (got day:{day}, year:{year})"
        )

    example = args.example
    config.EXAMPLE = example
    config.DEBUG = args.debug

    part_1 = args.part_1
    part_2 = args.part_2

    if not part_1 and not part_2:
        part_1 = part_2 = True

    if year == 0:
        years = sorted(
            int(module.name[-4:])
            for module in pkgutil.iter_modules(["aoc"])
            if module.name.startswith("aoc")
        )
    else:
        years = [year]

    for year in years:
        if day == 0:
            days = sorted(
                int(module.name[-2:])
                for module in pkgutil.iter_modules([f"aoc/aoc{year}"])
                if module.name.startswith("day")
            )
        else:
            days = [day]

        print(f"{year=} {days=}")
        for day_ in days:
            run_day(
                RunConfig(
                    year=year,
                    day=day_,
                    part_1=part_1,
                    part_2=part_2,
                    print_input=args.print_input,
                )
            )


def run_day(run_config: RunConfig) -> None:
    CONSOLE.print()
    CONSOLE.print(f"Running {run_config.year} day {run_config.day}", style="red bold")
    module_name = f"aoc.aoc{run_config.year}.day{run_config.day:02d}"
    CONSOLE.print(f"Loading {module_name}")

    try:
        day_module = import_module(module_name)
    except ModuleNotFoundError as e:
        CONSOLE.print(e)
        return

    with utils.timed("Load data"):
        data_raw = utils.load_data_raw(
            year=run_config.year, day=run_config.day, example=config.EXAMPLE
        )

    if run_config.print_input:
        CONSOLE.print("============= BEGIN INPUT =============")
        for line in data_raw:
            print(line)
        CONSOLE.print("============== END INPUT ==============")
        return

    try:
        parse_data = day_module.parse_data
    except AttributeError:
        CONSOLE.print("parse_data not found; using raw data")
        data = data_raw
    else:
        with utils.timed("Parse data"):
            data = parse_data(data_raw)

    if run_config.part_1:
        with utils.timed():
            answer = day_module.part1(data=data)
            CONSOLE.print()
            CONSOLE.print(f"Part 1: {answer}")

    if run_config.part_2:
        with utils.timed():
            answer = day_module.part2(data=data)
            CONSOLE.print()
            CONSOLE.print(f"Part 2: {answer}")


if __name__ == "__main__":
    main()
