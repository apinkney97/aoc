import asyncio
from enum import Enum

from aoc2019 import utils
from aoc2019.intcode import IntCodeProcessor, RunState


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


VECTORS = {
    Direction.NORTH: (0, -1),
    Direction.SOUTH: (0, 1),
    Direction.EAST: (1, 0),
    Direction.WEST: (-1, 0),
}


class Painter:
    def __init__(self, memory, start=0):
        self.processor = IntCodeProcessor(memory)
        self.panels = {}
        self.pos = (0, 0)
        self.panels[self.pos] = start
        self.direction = Direction.NORTH

        self._min_x = 0
        self._min_y = 0
        self._max_x = 0
        self._max_y = 0

    def move_left(self):
        self._move(-1)

    def move_right(self):
        self._move(1)

    def _move(self, direction: int):
        self.direction = Direction((self.direction.value + direction) % 4)

        x, y = self.pos
        dx, dy = VECTORS[self.direction]
        new_x = x + dx
        new_y = y + dy

        self._max_x = max(self._max_x, new_x)
        self._max_y = max(self._max_y, new_y)
        self._min_x = min(self._min_x, new_x)
        self._min_y = min(self._min_y, new_y)

        self.pos = new_x, new_y

    def __str__(self):
        bits = []
        for y in range(self._min_y, self._max_y + 1):
            for x in range(self._min_x, self._max_x + 1):
                value = self.panels.get((x, y), 0)
                bits.append({0: " ", 1: "\u2588"}[value] * 2)
            bits.append("\n")
        return "".join(bits)

    async def run(self) -> int:

        asyncio.create_task(self.processor.run())

        # Read in value of current pos
        # Read out colour to paint
        # Read out direction to turn (0 left, 1 right)

        while self.processor.state is not RunState.TERMINATED:
            old_colour = self.panels.get(self.pos, 0)
            await self.processor.input(old_colour)
            new_colour = await self.processor.output()
            self.panels[self.pos] = new_colour
            turn = await self.processor.output()
            if turn == 0:
                self.move_left()
            elif turn == 1:
                self.move_right()
            else:
                raise Exception(f"Bad turn direction {turn}")

        return len(self.panels)


async def run(start):
    memory = [int(i) for i in utils.load_data(11)[0].split(",")]
    painter = Painter(memory, start)
    result = await painter.run()
    print(str(painter))
    return result


def part1():
    return asyncio.run(run(0))


def part2():
    return asyncio.run(run(1))


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
