import re
import typing

import utils


class Sue(typing.NamedTuple):
    num: int
    children: int | None = None
    cats: int | None = None
    samoyeds: int | None = None
    pomeranians: int | None = None
    akitas: int | None = None
    vizslas: int | None = None
    goldfish: int | None = None
    trees: int | None = None
    cars: int | None = None
    perfumes: int | None = None


def load_data():
    data = utils.load_data(16, example=False)

    sues = []

    for line in data:
        match = re.fullmatch(
            r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line
        )
        num = match.group(1)
        prop1_name = match.group(2)
        prop1_val = int(match.group(3))
        prop2_name = match.group(4)
        prop2_val = int(match.group(5))
        prop3_name = match.group(6)
        prop3_val = int(match.group(7))

        sue_kwargs = {
            "num": num,
            prop1_name: prop1_val,
            prop2_name: prop2_val,
            prop3_name: prop3_val,
        }

        sues.append(Sue(**sue_kwargs))

    return sues


DATA = load_data()


MATCH_SUE = Sue(
    num=0,
    children=3,
    cats=7,
    samoyeds=2,
    pomeranians=3,
    akitas=0,
    vizslas=0,
    goldfish=5,
    trees=3,
    cars=2,
    perfumes=1,
)


def part1() -> int:

    sues = DATA

    for field in Sue._fields:
        if field == "num":
            continue
        sues = [
            s for s in sues if getattr(s, field) in {None, getattr(MATCH_SUE, field)}
        ]

    if len(sues) == 1:
        return sues[0].num

    return -1


def part2() -> int:
    sues = DATA

    # GT cats trees
    # LE pomeranians goldfish

    for field in Sue._fields:
        if field == "num":
            continue
        actual_val = getattr(MATCH_SUE, field)
        tmp_sues = []
        for sue in sues:
            val = getattr(sue, field)
            if val is None:
                tmp_sues.append(sue)
            else:
                if field in {"cats", "trees"}:
                    if val > actual_val:
                        tmp_sues.append(sue)
                elif field in {"pomeranians", "goldfish"}:
                    if val < actual_val:
                        tmp_sues.append(sue)
                else:
                    if val == actual_val:
                        tmp_sues.append(sue)
        sues = tmp_sues

    if len(sues) == 1:
        return sues[0].num

    return -1


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
