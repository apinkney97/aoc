from collections import defaultdict

from aoc2017.util import load_data


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

    def play(self):
        while True:
            inst, *args = self.instructions[self.program_counter]

            arg1 = args[0]
            arg2 = None

            if inst in {'snd', 'rcv', 'jgz'}:
                arg1 = self.resolve(arg1)
            if inst in {'set', 'add', 'mul', 'mod', 'jgz'}:
                arg2 = self.resolve(args[1])

            handler = getattr(self, 'handle_' + inst)
            if not handler(arg1, arg2):
                break

            self.program_counter += 1

            if self.program_counter >= len(self.instructions) or self.program_counter < 0:
                break


def part1():
    dp = DuetPlayer(get_instructions())
    dp.play()
    return dp.last_played


def part2():
    pass


if __name__ == '__main__':
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
