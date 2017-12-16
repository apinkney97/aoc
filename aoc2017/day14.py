from aoc2017.day10 import knot_hash

INPUT = 'jxqlasbh'


def get_grid():
    hashes = [knot_hash(INPUT + '-' + str(i)) for i in range(128)]
    return [list(bin(int(h, 16))[2:].zfill(128)) for h in hashes]


def part1():
    grid = get_grid()
    ones = 0
    for row in grid:
        ones += row.count('1')
    return ones


def part2():
    # TODO: Flood fill algorithm
    pass


if __name__ == '__main__':
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
