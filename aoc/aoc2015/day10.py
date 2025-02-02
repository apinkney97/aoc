type Data = str


def parse_data(data: list[str]) -> Data:
    return data[0]


def look_and_say(string: str) -> str:
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


def part1(data: Data) -> int:
    s = data
    for _ in range(40):
        s = look_and_say(s)

    return len(s)


def part2(data: Data) -> int:
    s = data
    for _ in range(50):
        s = look_and_say(s)

    return len(s)
