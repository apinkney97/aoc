import itertools
from enum import Enum


class Op(Enum):
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7


COMBO = {Op.adv, Op.bdv, Op.cdv, Op.bst, Op.out}


def dis(prog: list[int]) -> None:
    for operator, operand in itertools.batched(prog, 2):
        op = Op(operator)
        if op in COMBO and operand > 3:
            match operand:
                case 4:
                    operand = "A"
                case 5:
                    operand = "B"
                case 6:
                    operand = "C"

        match op:
            case Op.adv:
                print(f"A = A >> {operand}")
            case Op.bdv:
                print(f"B = A >> {operand}")
            case Op.cdv:
                print(f"C = A >> {operand}")
            case Op.bxl:
                print(f"B = B ^ {operand}")
            case Op.bst:
                print(f"B = {operand} % 8")
            case Op.jnz:
                print(f"JNZ {operand}")
            case Op.bxc:
                print("B = B ^ C")
            case Op.out:
                print(f"OUT {operand}")


class Computer:
    def __init__(self, a: int, b: int, c: int, program: list[int]) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.pc = 0
        self.out: list[int] = []

    def __str__(self):
        return f"Computer(a={self.a}, b={self.b}, c={self.c})"

    def evaluate_operand(self, op: Op, operand: int) -> int:
        if op not in COMBO or 0 <= operand <= 3:
            return operand

        match operand:
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c

        raise ValueError(f"Bad value {operand} for {op}")

    def run(self) -> list[int]:
        while self.pc < len(self.program):
            op = Op(self.program[self.pc])
            operand = self.evaluate_operand(op, self.program[self.pc + 1])

            match op:
                case Op.adv:
                    self.a = self.a >> operand
                case Op.bdv:
                    self.b = self.a >> operand
                case Op.cdv:
                    self.c = self.a >> operand
                case Op.bxl:
                    self.b = self.b ^ operand
                case Op.bst:
                    self.b = operand % 8
                case Op.jnz:
                    if self.a != 0:
                        self.pc = operand - 2
                case Op.bxc:
                    self.b = self.b ^ self.c
                case Op.out:
                    self.out.append(operand % 8)

            self.pc += 2

        return self.out


def parse_data(data):
    a = int(data[0].split()[-1])
    b = int(data[1].split()[-1])
    c = int(data[2].split()[-1])
    prog = [int(i) for i in data[4].split()[-1].split(",")]
    return Computer(a, b, c, prog)


def part1(data: Computer) -> str:
    computer = data
    result = computer.run()
    return ",".join(str(n) for n in result)


def part2(data) -> int:
    computer = data
    b = computer.b
    c = computer.c
    prog = computer.program

    dis(prog)

    top_digit_candidates = [0]

    for match_len in range(1, len(prog) + 1):
        digits = []

        for top_digits in top_digit_candidates:
            # Insight: a is consumed 3 bits at a time, and later output depends on most significant bits shifted right.
            # Trivial to try all 8 combos of 3 bits, shifting previously matched values along.
            for a in range(8):
                a = (top_digits << 3) | a
                result = Computer(a, b, c, prog).run()
                if result[-match_len:] == prog[-match_len:]:
                    digits.append(a)

        top_digit_candidates = digits

        # for digit in top_digit_candidates:
        #     print(f"{match_len}: {digit:o}")

    return min(top_digit_candidates)
