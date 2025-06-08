from __future__ import annotations

import asyncio
import typing
from collections import defaultdict
from typing import NamedTuple

type Data = list[Instruction]


class Instruction(NamedTuple):
    name: str
    arg_1: str
    arg_2: str | None = None


def parse_data(data: list[str]) -> Data:
    return [Instruction(*(line.split())) for line in data]


class BaseDuetPlayer:
    def __init__(self, instructions: Data) -> None:
        self.instructions = instructions
        self.registers: typing.DefaultDict[str, int] = defaultdict(int)
        self.program_counter = 0
        self._last_played: int | None = None

    @property
    def last_played(self) -> int:
        if self._last_played is None:
            raise Exception("No plays yet")
        return self._last_played

    def resolve(self, val_or_reg: str) -> int:
        try:
            return int(val_or_reg)
        except ValueError:
            pass
        return self.registers[val_or_reg]

    def handle_set(self, reg: str, val: str) -> bool:
        self.registers[reg] = self.resolve(val)
        return True

    def handle_add(self, reg: str, val: str) -> bool:
        self.registers[reg] += self.resolve(val)
        return True

    def handle_mul(self, reg: str, val: str) -> bool:
        self.registers[reg] *= self.resolve(val)
        return True

    def handle_mod(self, reg: str, val: str) -> bool:
        self.registers[reg] %= self.resolve(val)
        return True

    def handle_jgz(self, val: str, offset: str) -> bool:
        if self.resolve(val) > 0:
            self.program_counter += self.resolve(offset) - 1
        return True


class DuetPlayer(BaseDuetPlayer):
    def handle_snd(self, val: str, _: typing.Any) -> bool:
        self._last_played = self.resolve(val)
        return True

    def handle_rcv(self, val: str, _: typing.Any) -> bool:
        return self.resolve(val) == 0

    def play(self) -> None:
        while True:
            instruction = self.instructions[self.program_counter]

            handler = getattr(self, "handle_" + instruction.name)
            if not handler(instruction.arg_1, instruction.arg_2):
                break

            self.program_counter += 1

            if (
                self.program_counter >= len(self.instructions)
                or self.program_counter < 0
            ):
                break


DEADLOCK_SENTINEL = None


class AsyncDuetPlayer(BaseDuetPlayer):
    def __init__(
        self, instructions: Data, p: int, queue: asyncio.Queue[int | None]
    ) -> None:
        super().__init__(instructions)
        self.id = p
        self.registers["p"] = p
        self.queue = queue
        self.send_count = 0
        self.is_waiting = False

        self.other = self

    async def handle_snd(self, val: str, _: typing.Any) -> bool:
        self.other.queue.put_nowait(self.resolve(val))
        self.send_count += 1
        return True

    async def handle_rcv(self, reg: str, _: typing.Any) -> bool:
        if self.other.is_waiting and self.queue.empty() and self.other.queue.empty():
            self.other.queue.put_nowait(DEADLOCK_SENTINEL)
            return False

        self.is_waiting = True
        val = await self.queue.get()
        self.is_waiting = False

        if val is DEADLOCK_SENTINEL:
            return False

        self.registers[reg] = val
        return True

    async def play(self) -> None:
        while True:
            instruction = self.instructions[self.program_counter]

            handler = getattr(self, "handle_" + instruction.name)
            res = handler(instruction.arg_1, instruction.arg_2)

            if instruction.name in {"rcv", "snd"}:
                res = await res

            if not res:
                break

            self.program_counter += 1

            if (
                self.program_counter >= len(self.instructions)
                or self.program_counter < 0
            ):
                break


def part1(data: Data) -> int:
    dp = DuetPlayer(data)
    dp.play()
    return dp.last_played


def part2(data: Data) -> int:
    return asyncio.run(_part2(data))


async def _part2(data: Data) -> int:
    queue0: asyncio.Queue[int | None] = asyncio.Queue()
    queue1: asyncio.Queue[int | None] = asyncio.Queue()

    dp0 = AsyncDuetPlayer(data, 0, queue0)
    dp1 = AsyncDuetPlayer(data, 1, queue1)
    dp0.other = dp1
    dp1.other = dp0

    await asyncio.gather(dp0.play(), dp1.play())

    return dp1.send_count
