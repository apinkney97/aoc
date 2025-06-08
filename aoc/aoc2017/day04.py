from collections.abc import Callable

type Data = list[str]


def contains_dupes(words: list[str]) -> bool:
    return len(words) != len(set(words))


def contains_anags(words: list[str]) -> bool:
    words = ["".join(sorted(word)) for word in words]
    return contains_dupes(words)


def get_valid_count(data: Data, invalidation_fn: Callable[[list[str]], bool]) -> int:
    count = 0
    for line in data:
        words = line.strip().split(" ")
        if not invalidation_fn(words):
            count += 1
    return count


def part1(data: Data) -> int:
    return get_valid_count(data, contains_dupes)


def part2(data: Data) -> int:
    return get_valid_count(data, contains_anags)
