from collections import Counter

type Data = tuple[list[int], list[int]]


def parse_data(data: list[str]) -> Data:
    left = []
    right = []
    for line in data:
        left_item, right_item = line.split()
        left.append(int(left_item))
        right.append(int(right_item))
    return left, right


def part1(data: Data) -> int:
    left, right = data
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def part2(data: Data) -> int:
    left, right = data
    right_counts = Counter(right)
    return sum(i * right_counts[i] for i in left)
