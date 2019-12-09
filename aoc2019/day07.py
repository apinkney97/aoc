import asyncio
from itertools import cycle, permutations

from aoc2019 import utils
from aoc2019.intcode import IntCodeProcessor, RunState


async def intcode_eval(phase_settings) -> int:
    memory = [int(i) for i in utils.load_data(7)[0].split(",")]
    processors = []

    for phase_setting in phase_settings:
        processor = IntCodeProcessor(memory)
        processors.append(processor)
        asyncio.create_task(processor.run())
        await processor.input(phase_setting)

    output = 0
    for processor in cycle(processors):
        if processor.state is RunState.TERMINATED:
            break
        await processor.input(output)
        output = await processor.output()

    return output


def part1():
    max_ = None
    for phase_settings in permutations(range(5), 5):
        max_ = utils.safe_max(max_, asyncio.run(intcode_eval(phase_settings)))

    return max_


def part2():
    max_ = None
    for phase_settings in permutations(range(5, 10), 5):
        max_ = utils.safe_max(max_, asyncio.run(intcode_eval(phase_settings)))

    return max_


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
