type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(i) for i in data[0].split("\t")]


def part1(data: Data) -> int:
    banks = data[:]
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


def part2(data: Data) -> int:
    banks = data[:]
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
