import re
import typing

from aoc import utils

# EXAMPLE = True
EXAMPLE = False


class Move(typing.NamedTuple):
    num: int
    src: int
    dst: int


def load_data():
    data = utils.load_data(2022, 5, example=EXAMPLE, strip=False)
    d_it = iter(data)
    stack_rows = []
    for row in d_it:
        row = row.strip("\n")
        if not row:
            break
        stack_rows.append(row)

    stacks = [[] for _ in range(10)]

    for row in reversed(stack_rows[:-1]):
        for i, c in enumerate(row):
            if i % 4 - 1 == 0 and c != " ":
                stack_num = (i - 1) // 4 + 1
                stacks[stack_num].append(c)

    moves = []
    for row in d_it:
        match = re.fullmatch(
            r"move (?P<num>\d+) from (?P<src>\d+) to (?P<dst>\d+)", row.strip()
        )
        moves.append(
            Move(num=int(match["num"]), src=int(match["src"]), dst=int(match["dst"]))
        )

    return stacks, moves


def get_tops(stacks: list[list[str]]) -> str:
    tops = []
    for stack in stacks[1:]:
        if stack:
            tops.append(stack[-1])
        else:
            tops.append(" ")
    return "".join(tops)


def part1() -> str:
    stacks, moves = load_data()

    for move in moves:
        for _ in range(move.num):
            stacks[move.dst].append(stacks[move.src].pop())

    return get_tops(stacks)


def part2() -> str:
    stacks, moves = load_data()
    for move in moves:
        tmp_stack = []
        for _ in range(move.num):
            tmp_stack.append(stacks[move.src].pop())
        for item in tmp_stack[::-1]:
            stacks[move.dst].append(item)

    return get_tops(stacks)


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
