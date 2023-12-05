import utils


def _get_data():
    data = utils.load_data(2020, 10, fn=int, example=False) + [0]
    data.sort()
    data.append(data[-1] + 3)
    return data


DATA = _get_data()


def part1() -> int:
    ones = 0
    threes = 0
    for i, j in zip(DATA, DATA[1:]):
        diff = j - i
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1

    return ones * threes


def part2() -> int:
    # Diffs only seem to be 3 or 1
    # Can't remove any with a diff of 3
    # Can remove any with a diff of 1 as long as the remaining gap is <= 3
    # Find number of possible permutations of removing numbers in runs with diffs of 1
    # if the run is len 1-2, can remove either/both, so all perms valid
    # if the run is len 3, can't remove all of them at once.
    # don't appear to be any runs longer than 3

    arrangements = 1
    curr = []
    for i, j, k in zip(DATA, DATA[1:], DATA[2:]):
        lower_diff = j - i
        upper_diff = k - j

        if lower_diff == upper_diff == 1:
            curr.append(j)
        else:
            if curr:
                perms = 2 ** len(curr)
                if len(curr) == 3:
                    perms -= 1  # discount case where all are removed
                arrangements *= perms
                # print("    ", len(curr), curr)
                curr = []

        # print(lower_diff, upper_diff, "  ", i, j, k)

    return arrangements


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
