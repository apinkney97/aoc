from aoc import utils

type Data = tuple[dict[int, set[int]], list[list[int]]]


def parse_data(data: list[str]) -> Data:
    rules, runs = utils.split_by_blank_lines(data)

    rule_map: dict[int, set[int]] = {}
    for rule in rules:
        before, after = rule.split("|")
        rule_map.setdefault(int(after), set()).add(int(before))

    parsed_runs = []
    for run in runs:
        parsed_runs.append([int(n) for n in run.split(",")])

    return rule_map, parsed_runs


def is_valid(run: list[int], rules: dict[int, set[int]]) -> bool:
    for i, current in enumerate(run):
        forbidden_after = rules.get(current, set())
        for after in run[i + 1 :]:
            if after in forbidden_after:
                return False
    return True


def part1(data: Data) -> int:
    result = 0
    rules, runs = data

    for run in runs:
        if is_valid(run, rules):
            result += run[len(run) // 2]

    return result


def get_first(numbers: set[int], rules: dict[int, set[int]]) -> tuple[int, set[int]]:
    for n in numbers:
        forbidden_after = rules.get(n, set())
        remaining_numbers = set(numbers)
        remaining_numbers.remove(n)

        if not remaining_numbers & forbidden_after:
            return n, remaining_numbers
    raise ValueError


def part2(data: Data) -> int:
    result = 0
    rules, runs = data

    for run in runs:
        if not is_valid(run, rules):
            remaining = set(run)
            current = 0
            for _ in range(len(run) // 2 + 1):
                current, remaining = get_first(remaining, rules)
            result += current

    return result
