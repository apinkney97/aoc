import itertools
import re

import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(19, example=EXAMPLE)
    rules = {}
    for line in data:
        if not line:
            break
        src, dst = line.split(" => ")
        rules.setdefault(src, []).append(dst)

    molecule = data[-1]
    return molecule, rules


DATA = load_data()


def part1() -> int:
    input_mol, rules = DATA

    new_molecules = set()

    for src in rules:
        for match in re.finditer(src, input_mol):
            start = match.start()
            end = match.end()
            for dst in rules[src]:
                new_molecule = input_mol[:start] + dst + input_mol[end:]
                new_molecules.add(new_molecule)

    return len(new_molecules)


def part2() -> int:
    target = DATA[0]
    inverted_rules: dict[str, str] = {}
    for src in DATA[1]:
        for dst in DATA[1][src]:
            inverted_rules[dst] = src

    sorted_rules: list[str] = sorted(inverted_rules, key=len)
    sorted_rules.reverse()

    steps = []

    current = target
    for n in itertools.count(1):
        for rule in sorted_rules:
            if rule in current:
                steps.append((rule, inverted_rules[rule], current))
                current = current.replace(rule, inverted_rules[rule], 1)
                if current == "e":
                    return n
                break
        else:
            print("No rule applied :(")
            print(n, current)
            break

    return -1


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
