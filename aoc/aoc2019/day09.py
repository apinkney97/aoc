import asyncio

from aoc.aoc2019.intcode import Data, IntCodeProcessor, parse_data  # noqa: F401


async def intcode_eval(memory: Data, auto_input: list[int]) -> int:
    processor = IntCodeProcessor(memory, verbosity=1)

    for i in auto_input:
        await processor.input(i)
    result = await processor.run(return_last_output=True)
    assert result is not None
    return result


def part1(data: Data) -> int:
    return asyncio.run(intcode_eval(data, [1]))


def part2(data: Data) -> int:
    return asyncio.run(intcode_eval(data, [2]))
