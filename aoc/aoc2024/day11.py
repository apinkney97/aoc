from collections import Counter

type Data = list[int]


def parse_data(data: list[str]) -> Data:
    return [int(i) for i in data[0].split()]


def part1(data: Data, blinks: int = 25) -> int:
    stones: Counter[int] = Counter(data)

    for _ in range(blinks):
        new_stones: Counter[int] = Counter()

        for stone_val, count in stones.items():
            if stone_val == 0:
                new_stones[1] += count
            elif len(str(stone_val)) % 2 == 0:
                stone_val_str = str(stone_val)
                midpoint = len(stone_val_str) // 2
                new_stones[int(stone_val_str[:midpoint])] += count
                new_stones[int(stone_val_str[midpoint:])] += count
            else:
                new_stones[stone_val * 2024] += count

        stones = new_stones

    return sum(stones.values())


def part2(data: Data) -> int:
    return part1(data, blinks=75)
