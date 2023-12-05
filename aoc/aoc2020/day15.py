DATA = [6, 4, 12, 1, 20, 0, 16]

# DATA = [0, 3, 6]
# DATA = [1, 3, 2]
# DATA = [2, 1, 3]
# DATA = [1, 2, 3]
# DATA = [2, 3, 1]
# DATA = [3, 2, 1]
# DATA = [3, 1, 2]


def mem_game(n):
    seen = {}
    for i, d in enumerate(DATA):
        seen.setdefault(d, []).append(i)

    last = DATA[-1]
    for i in range(len(DATA), n):
        last_seen = seen.get(last, [])
        if len(last_seen) < 2:
            new_val = 0
        else:
            new_val = last_seen[-1] - last_seen[-2]
        last = new_val
        seen.setdefault(new_val, []).append(i)

    return last


def part1() -> int:
    return mem_game(2020)


def part2() -> int:
    return mem_game(30000000)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
