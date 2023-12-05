from collections import defaultdict

from aoc import utils

CMP_FNS = {
    "==": lambda a, b: a == b,
    "!=": lambda a, b: a != b,
    "<=": lambda a, b: a <= b,
    ">=": lambda a, b: a >= b,
    "<": lambda a, b: a < b,
    ">": lambda a, b: a > b,
}

GLOBAL_MAX = 0


def do_work():
    global GLOBAL_MAX
    cells = defaultdict(int)
    for line in utils.load_data(2017, 8):
        this_name, action, val, _, that, cmp_op, cmp_val = line.split(" ")
        cmp_val = int(cmp_val)
        if CMP_FNS[cmp_op](cells[that], cmp_val):
            val = int(val)
            if action == "inc":
                cells[this_name] += val
            elif action == "dec":
                cells[this_name] -= val

            if cells[this_name] > GLOBAL_MAX:
                GLOBAL_MAX = cells[this_name]

    return max(cells.values())


if __name__ == "__main__":
    print("Part 1: {}".format(do_work()))
    print("Part 2: {}".format(GLOBAL_MAX))
