from aoc2017.util import load_data

MUL_A = 16807
MUL_B = 48271
MOD = 2147483647
MASK = 2**16 - 1


def gen(start, mul, mod=1):
    val = start
    while True:
        val = (val * mul) % MOD
        if val % mod == 0:
            yield val


def part1(a_start, b_start):
    a_gen = gen(a_start, MUL_A)
    b_gen = gen(b_start, MUL_B)
    count = 0
    for _ in range(40000000):
        if next(a_gen) & MASK == next(b_gen) & MASK:
            count += 1
    return count


def part2(a_start, b_start):
    a_gen = gen(a_start, MUL_A, 4)
    b_gen = gen(b_start, MUL_B, 8)
    count = 0
    for _ in range(5000000):
        if next(a_gen) & MASK == next(b_gen) & MASK:
            count += 1
    return count


if __name__ == "__main__":
    a, b = (int(line.rsplit(" ", 1)[1]) for line in load_data(15))
    print("Part 1: {}".format(part1(a, b)))
    print("Part 2: {}".format(part2(a, b)))
