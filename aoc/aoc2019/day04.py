INPUT = [146810, 612564]
PASSCODE_LEN = 6


def is_valid(passcode: int, strict_doubles=False) -> bool:
    passcode = list(str(passcode))

    if len(passcode) != PASSCODE_LEN:
        return False

    if sorted(passcode) != passcode:
        return False

    for i in range(PASSCODE_LEN - 1):
        digit = passcode[i]

        if digit == passcode[i + 1]:
            if not strict_doubles:
                # We don't care if the double is part of a longer run
                return True

            if i > 0 and passcode[i - 1] == digit:
                # doesn't count if the digit preceding the pair is the same
                continue

            if i < PASSCODE_LEN - 2 and passcode[i + 2] == digit:
                # doesn't count if the digit after the pair is the same
                continue

            return True


def part1() -> int:
    valid_count = 0
    for i in range(*INPUT):
        if is_valid(i):
            valid_count += 1
    return valid_count


def part2() -> int:
    valid_count = 0
    for i in range(*INPUT):
        if is_valid(i, strict_doubles=True):
            valid_count += 1
    return valid_count


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
