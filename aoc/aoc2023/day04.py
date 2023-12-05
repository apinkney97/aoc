from aoc import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(2023, 4, example=EXAMPLE)
    card_wins = []
    for line in data:
        numbers = line.split(":")[1]
        winning, ours = numbers.split("|")
        card_wins.append(len(set(winning.split()) & set(ours.split())))

    return card_wins


with utils.timed("Load data"):
    DATA = load_data()


def part1() -> int:
    total = 0
    for wins in DATA:
        if wins:
            total += 2 ** (wins - 1)
    return total


def part2() -> int:
    counts = [1] * len(DATA)
    for card_id, wins in enumerate(DATA):
        num_copies = counts[card_id]
        for new_card in range(card_id + 1, card_id + wins + 1):
            counts[new_card] += num_copies
    return sum(counts)


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
