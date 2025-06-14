from collections import Counter

type Data = list[str]


def parse_data(data: list[str]) -> Data:
    return data


def part1(data: Data) -> str:
    counters = [Counter(letters) for letters in zip(*data)]
    return "".join(c.most_common(1)[0][0] for c in counters)


def part2(data: Data) -> str:
    counters = [Counter(letters) for letters in zip(*data)]
    return "".join(c.most_common()[-1][0] for c in counters)
