import itertools
import re

type Data = tuple[str, dict[str, list[str]]]


def parse_data(data: list[str]) -> Data:
    rules: dict[str, list[str]] = {}
    for line in data:
        if not line:
            break
        src, dst = line.split(" => ")
        rules.setdefault(src, []).append(dst)

    molecule = data[-1]
    return molecule, rules


def part1(data: Data) -> int:
    input_mol, rules = data

    new_molecules = set()

    for src in rules:
        for match in re.finditer(src, input_mol):
            start = match.start()
            end = match.end()
            for dst in rules[src]:
                new_molecule = input_mol[:start] + dst + input_mol[end:]
                new_molecules.add(new_molecule)

    return len(new_molecules)


def part2(data: Data) -> int:
    target = data[0]
    inverted_rules: dict[str, str] = {}
    for src in data[1]:
        for dst in data[1][src]:
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
