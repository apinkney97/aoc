import asyncio
from itertools import permutations

from aoc2019 import utils
from aoc2019.day05 import IntCodeProcessor


async def intcode_eval(phase_settings) -> int:
    memory = [int(i) for i in utils.load_data(7)[0].split(",")]
    processors = [IntCodeProcessor(memory) for _ in phase_settings]

    output = 0
    for processor, phase_setting in zip(processors, phase_settings):
        await processor.input(phase_setting)
        await processor.input(output)
        output = await processor.run()

    return output


def get_phase_settings():
    return permutations(range(5), 5)


def part1():
    max_ = None
    for phase_settings in get_phase_settings():
        max_ = utils.safe_max(max_, asyncio.run(intcode_eval(phase_settings)))

    return max_


def part2():
    pass


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
