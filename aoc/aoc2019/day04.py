PASSCODE_LEN = 6

type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(i) for i in data[0].split("-")]


def is_valid(passcode: int, strict_doubles: bool = False) -> bool:
    passcode_digits = list(str(passcode))

    if len(passcode_digits) != PASSCODE_LEN:
        return False

    if sorted(passcode_digits) != passcode_digits:
        return False

    for i in range(PASSCODE_LEN - 1):
        digit = passcode_digits[i]

        if digit == passcode_digits[i + 1]:
            if not strict_doubles:
                # We don't care if the double is part of a longer run
                return True

            if i > 0 and passcode_digits[i - 1] == digit:
                # doesn't count if the digit preceding the pair is the same
                continue

            if i < PASSCODE_LEN - 2 and passcode_digits[i + 2] == digit:
                # doesn't count if the digit after the pair is the same
                continue

            return True

    return False


def part1(data: Data) -> int:
    valid_count = 0
    for i in range(data[0], data[1]):
        if is_valid(i):
            valid_count += 1
    return valid_count


def part2(data: Data) -> int:
    valid_count = 0
    for i in range(data[0], data[1]):
        if is_valid(i, strict_doubles=True):
            valid_count += 1
    return valid_count
