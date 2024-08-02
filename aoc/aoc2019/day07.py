import asyncio
from itertools import cycle, permutations

from aoc import utils
from aoc.aoc2019.intcode import IntCodeProcessor, RunState
from aoc.aoc2019.intcode import parse_data as parse_data


async def intcode_eval(memory, phase_settings) -> int:
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


def part1(data):
    max_ = None
    for phase_settings in permutations(range(5), 5):
        max_ = utils.safe_max(max_, asyncio.run(intcode_eval(data, phase_settings)))

    return max_


def part2(data):
    max_ = None
    for phase_settings in permutations(range(5, 10), 5):
        max_ = utils.safe_max(max_, asyncio.run(intcode_eval(data, phase_settings)))

    return max_
