import asyncio

from aoc.aoc2019.intcode import IntCodeProcessor
from aoc.aoc2019.intcode import parse_data as parse_data


async def intcode_eval(memory, auto_input: list[int]) -> int:
    processor = IntCodeProcessor(memory, verbosity=1)

    for i in auto_input:
        await processor.input(i)
    return await processor.run(return_last_output=True)


def part1(data):
    return asyncio.run(intcode_eval(data, [1]))


def part2(data):
    return asyncio.run(intcode_eval(data, [2]))
