def parse_data(data):
    card_wins = []
    for line in data:
        numbers = line.split(":")[1]
        winning, ours = numbers.split("|")
        card_wins.append(len(set(winning.split()) & set(ours.split())))

    return card_wins


def part1(data) -> int:
    total = 0
    for wins in data:
        if wins:
            total += 2 ** (wins - 1)
    return total


def part2(data) -> int:
    counts = [1] * len(data)
    for card_id, wins in enumerate(data):
        num_copies = counts[card_id]
        for new_card in range(card_id + 1, card_id + wins + 1):
            counts[new_card] += num_copies
    return sum(counts)
