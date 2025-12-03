type Data = list[list[int]]


def parse_data(data: list[str]) -> Data:
    parsed = []
    for line in data:
        parsed.append([int(i) for i in line])
    return parsed


def part1(data: Data) -> int:
    result = 0
    for bank in data:
        first, bank = joltage(bank, 2)
        second, bank = joltage(bank, 1)
        result += int(f"{first}{second}")

    return result


def part2(data: Data) -> int:
    result = 0
    for bank in data:
        joltages = []
        for i in range(12, 0, -1):
            j, bank = joltage(bank, i)
            joltages.append(j)
        best = int("".join(str(j) for j in joltages))
        result += best
    return result


def joltage(bank: list[int], size: int) -> tuple[int, list[int]]:
    index = -(size - 1) or None
    value = max(bank[:index])
    remaining_bank = bank[bank.index(value) + 1 :]
    return value, remaining_bank
