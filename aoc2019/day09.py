import asyncio
from typing import List

import utils
from aoc2019.intcode import IntCodeProcessor


async def intcode_eval(auto_input: List[int] = None) -> int:
    memory = [int(i) for i in utils.load_data(2019, 9)[0].split(",")]
    processor = IntCodeProcessor(memory, verbosity=1)

    for i in auto_input:
        await processor.input(i)
    return await processor.run(return_last_output=True)


def part1():
    return asyncio.run(intcode_eval([1]))


def part2():
    return asyncio.run(intcode_eval([2]))


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
