import utils

DATA = utils.load_data(2015, 10)


def look_and_say(string: str):
    count = 1
    curr = None
    out = []

    for char in string:
        if curr != char:
            if curr is not None:
                out.append((curr, count))
            curr = char
            count = 1
        else:
            count += 1

    out.append((curr, count))

    return "".join(f"{count}{char}" for char, count in out)


def part1() -> int:
    s = DATA[0]
    for _ in range(40):
        s = look_and_say(s)

    return len(s)


def part2() -> int:
    s = DATA[0]
    for _ in range(50):
        s = look_and_say(s)

    return len(s)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
