A_START = 783
B_START = 325
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


def part1():
    a_gen = gen(A_START, MUL_A)
    b_gen = gen(B_START, MUL_B)
    count = 0
    for _ in range(40000000):
        if next(a_gen) & MASK == next(b_gen) & MASK:
            count += 1
    return count


def part2():
    a_gen = gen(A_START, MUL_A, 4)
    b_gen = gen(B_START, MUL_B, 8)
    count = 0
    for _ in range(5000000):
        if next(a_gen) & MASK == next(b_gen) & MASK:
            count += 1
    return count


if __name__ == '__main__':
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
