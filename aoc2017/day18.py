import asyncio
from collections import defaultdict

from aoc2017.util import load_data

event_loop = asyncio.get_event_loop()


def get_instructions():
    instructions = []

    def try_int(val):
        try:
            return int(val)
        except ValueError:
            return val

    for line in load_data(18):
        instructions.append(tuple(try_int(v) for v in line.split(' ')))

    return instructions


class DuetPlayer:
    def __init__(self, instructions):
        self.instructions = instructions
        self.registers = defaultdict(int)
        self.program_counter = 0
        self.last_played = None

        self.resolve_arg_1 = {'snd', 'rcv', 'jgz'}
        self.resolve_arg_2 = {'set', 'add', 'mul', 'mod', 'jgz'}

    def resolve(self, val_or_reg):
        if isinstance(val_or_reg, int):
            return val_or_reg
        return self.registers[val_or_reg]

    def handle_snd(self, val, _):
        self.last_played = val
        return True

    def handle_set(self, reg, val):
        self.registers[reg] = val
        return True

    def handle_add(self, reg, val):
        self.registers[reg] += val
        return True

    def handle_mul(self, reg, val):
        self.registers[reg] *= val
        return True

    def handle_mod(self, reg, val):
        self.registers[reg] %= val
        return True

    def handle_rcv(self, val, _):
        return val == 0

    def handle_jgz(self, val, offset):
        if val > 0:
            self.program_counter += (offset - 1)
        return True

    def get_instruction(self):
        inst, *args = self.instructions[self.program_counter]
        arg1 = args[0]
        arg2 = None
        if inst in self.resolve_arg_1:
            arg1 = self.resolve(arg1)
        if inst in self.resolve_arg_2:
            arg2 = self.resolve(args[1])
        return inst, arg1, arg2

    def play(self):
        while True:
            inst, arg1, arg2 = self.get_instruction()

            handler = getattr(self, 'handle_' + inst)
            if not handler(arg1, arg2):
                break

            self.program_counter += 1

            if self.program_counter >= len(self.instructions) or self.program_counter < 0:
                break


deadlock_sentinel = object()


class AsyncDuetPlayer(DuetPlayer):
    def __init__(self, instructions, p, queue, other):
        super().__init__(instructions)
        self.resolve_arg_1 = {'snd', 'jgz'}
        self.id = p
        self.registers['p'] = p
        self.queue = queue
        self.other = other
        self.send_count = 0
        self.is_waiting = False

    async def handle_snd(self, val, _):
        self.other.queue.put_nowait(val)
        self.send_count += 1
        return True

    async def handle_rcv(self, reg, _):
        if self.other.is_waiting and self.queue.empty() and self.other.queue.empty():
            self.other.queue.put_nowait(deadlock_sentinel)
            return False
        self.is_waiting = True
        val = await self.queue.get()
        self.is_waiting = False
        if val is deadlock_sentinel:
            return False
        self.registers[reg] = val
        return True

    async def play(self):
        while True:
            inst, arg1, arg2 = self.get_instruction()

            handler = getattr(self, 'handle_' + inst)
            if inst in {'rcv', 'snd'}:
                if not await handler(arg1, arg2):
                    break
            else:
                handler(arg1, arg2)

            self.program_counter += 1

            if self.program_counter >= len(self.instructions) or self.program_counter < 0:
                break


def part1():
    dp = DuetPlayer(get_instructions())
    dp.play()
    return dp.last_played


async def part2():
    instructions = get_instructions()
    queue0 = asyncio.Queue()
    queue1 = asyncio.Queue()

    dp0 = AsyncDuetPlayer(instructions, 0, queue0, None)
    dp1 = AsyncDuetPlayer(instructions, 1, queue1, dp0)
    dp0.other = dp1

    await asyncio.gather(dp0.play(), dp1.play())

    return dp1.send_count


if __name__ == '__main__':
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(event_loop.run_until_complete(part2())))
    event_loop.close()
