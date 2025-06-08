import asyncio
from itertools import cycle, permutations
from typing import Collection

from aoc.aoc2019.intcode import (
    Data,
    IntCodeProcessor,
    RunState,
    parse_data,  # noqa: F401
)


async def intcode_eval(memory: Data, phase_settings: Collection[int]) -> int:
    processors = []

    tasks = set()
    for phase_setting in phase_settings:
        processor = IntCodeProcessor(memory)
        processors.append(processor)
        task = asyncio.create_task(processor.run())
        tasks.add(task)
        task.add_done_callback(tasks.discard)
        await processor.input(phase_setting)

    output = 0
    for processor in cycle(processors):
        if processor.state is RunState.TERMINATED:
            break
        await processor.input(output)
        output = await processor.output()

    return output


def part1(data: Data) -> int:
    results = []
    for phase_settings in permutations(range(5), 5):
        results.append(asyncio.run(intcode_eval(data, phase_settings)))

    return max(results)


def part2(data: Data) -> int:
    results = []
    for phase_settings in permutations(range(5, 10), 5):
        results.append(asyncio.run(intcode_eval(data, phase_settings)))

    return max(results)
