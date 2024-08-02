from collections import Counter


def parse_data(data):
    template = list(data[0])

    rules = {}
    for line in data[2:]:
        k, v = line.split(" -> ")
        rules[tuple(k)] = v

    return template, rules


def part1(data) -> int:
    template, rules = data

    polymer = template

    for i in range(10):
        new = [polymer[0]]
        for pair in zip(polymer, polymer[1:]):
            new.append(rules[pair])
            new.append(pair[1])
        polymer = new

    c = Counter(polymer)
    return max(c.values()) - min(c.values())


def part2(data) -> int:
    # every AB -> C construction:
    #   reduces AB pairs by 1
    #   increases AC and BC pairs by 1
    template, rules = data
    pairs = Counter(zip(template, template[1:]))

    for _ in range(40):
        new_pairs = pairs.copy()
        for pair, count in pairs.items():
            if pair in rules:
                new_pairs[pair] -= count
                new_pairs[(pair[0], rules[pair])] += count
                new_pairs[(rules[pair], pair[1])] += count
        pairs = new_pairs

    individuals = Counter([template[0]])
    for pair, count in pairs.items():
        individuals[pair[1]] += count
    return max(individuals.values()) - min(individuals.values())
