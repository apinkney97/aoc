from collections import Counter


def parse_data(data):
    return [int(i) for i in data[0].split()]


def part1(data, blinks=25) -> int:
    stones = Counter(data)

    for _ in range(blinks):
        new_stones = Counter()

        for stone_val, count in stones.items():
            if stone_val == 0:
                new_stones[1] += count
            elif len(str(stone_val)) % 2 == 0:
                stone_val = str(stone_val)
                midpoint = len(stone_val) // 2
                new_stones[int(stone_val[:midpoint])] += count
                new_stones[int(stone_val[midpoint:])] += count
            else:
                new_stones[stone_val * 2024] += count

        stones = new_stones

    return sum(stones.values())


def part2(data) -> int:
    return part1(data, blinks=75)
