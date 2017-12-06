DATA = "4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5"


def get_data():
    return [int(i) for i in DATA.split('\t')]


def part1():
    banks = get_data()
    # banks = [0, 2, 7, 0]
    seen = {tuple(banks)}

    while True:
        value = max(banks)
        index = banks.index(value)
        banks[index] = 0
        while value:
            index = (index + 1) % len(banks)
            banks[index] += 1
            value -= 1

        state = tuple(banks)
        if state in seen:
            return len(seen)
        seen.add(state)


def part2():
    banks = get_data()
    # banks = [0, 2, 7, 0]
    seen = {tuple(banks): 0}

    while True:
        value = max(banks)
        index = banks.index(value)
        banks[index] = 0
        while value:
            index = (index + 1) % len(banks)
            banks[index] += 1
            value -= 1

        state = tuple(banks)
        if state in seen:
            return len(seen) - seen[state]
        seen[state] = len(seen)


if __name__ == '__main__':
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
