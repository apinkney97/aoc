import asyncio
from collections import Counter
from enum import Enum
from typing import MutableMapping, NamedTuple

from aoc import utils
from aoc.aoc2019 import intcode
from aoc.aoc2019.intcode import parse_data as parse_data

# 0 is an empty tile. No game object appears in this tile.
# 1 is a wall tile. Walls are indestructible barriers.
# 2 is a block tile. Blocks can be broken by the ball.
# 3 is a horizontal paddle tile. The paddle is indestructible.
# 4 is a ball tile. The ball moves diagonally and bounces off objects.


class Tile(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


class Coord(NamedTuple):
    x: int
    y: int


DISP = {
    Tile.EMPTY: utils.BACKGROUND_BLOCK,
    Tile.WALL: "##",
    Tile.BLOCK: utils.FOREGROUND_BLOCK,
    Tile.PADDLE: "==",
    Tile.BALL: "{}",
}


class Arcade:
    def __init__(self, memory, add_credit=False):
        if add_credit:
            memory[0] = 2
        self._grid: MutableMapping[Coord, Tile] = {}
        self._processor = intcode.IntCodeProcessor(memory, verbosity=0)
        self._ball_x = 0
        self._paddle_x = 0

        self._grid = {}
        self._score = 0
        self._min_x = None
        self._max_x = None
        self._min_y = None
        self._max_y = None

    @property
    def score(self):
        return self._score

    @property
    def block_count(self):
        return Counter(self._grid.values())[Tile.BLOCK]

    def __str__(self):
        score = f"## Score: {self.score} ##"
        top = "#" * len(score)
        bits = [top, "\n", score, "\n"]
        for y in range(self._min_y, self._max_y + 1):
            for x in range(self._min_x, self._max_x + 1):
                tile = self._grid.get(Coord(x, y), Tile.EMPTY)
                bits.append(DISP[tile])
            bits.append("\n")
        return "".join(bits)

    async def _read_board_state(self):
        blocks_read = 0
        utils.log(f"{self._processor.state=} {self._processor.has_output()=}")
        while (
            self._processor.state
            not in {intcode.RunState.TERMINATED, intcode.RunState.AWAITING_INPUT}
            or self._processor.has_output()
            or blocks_read == 0
        ):
            x = await self._processor.output()
            y = await self._processor.output()
            tile_id = await self._processor.output()

            blocks_read += 1

            if x == -1 and y == 0:
                self._score = tile_id
                continue

            coord = Coord(x, y)
            tile = Tile(tile_id)
            self._grid[coord] = tile

            if tile is Tile.BALL:
                self._ball_x = x
            elif tile is Tile.PADDLE:
                self._paddle_x = x

            self._min_x = utils.safe_min(self._min_x, x)
            self._max_x = utils.safe_max(self._max_x, x)
            self._min_y = utils.safe_min(self._min_y, y)
            self._max_y = utils.safe_max(self._max_y, y)
        # utils.log(f"{blocks_read=} {self._grid=}")

    async def run(self):
        _ = asyncio.create_task(self._processor.run())
        await self._read_board_state()
        utils.log("Part 1:", Counter(self._grid.values())[Tile.BLOCK])
        utils.log(str(self))

        while self._processor.state is not intcode.RunState.TERMINATED:
            utils.log(f"{self._ball_x=} {self._paddle_x=}")
            if self._ball_x < self._paddle_x:
                inp = -1
                utils.log("MOVING LEFT")
            elif self._ball_x > self._paddle_x:
                inp = 1
                utils.log("MOVING RIGHT")
            else:
                inp = 0
                utils.log("NOT MOVING")
            await self._processor.input(inp)
            await self._read_board_state()
            utils.log(str(self))


async def run(memory, add_credit: bool):
    arcade = Arcade(memory, add_credit=add_credit)
    await arcade.run()
    return arcade


def part1(data):
    return asyncio.run(run(data, add_credit=False)).block_count


def part2(data):
    return asyncio.run(run(data, add_credit=True)).score
