import re


def parse_data(data):
    it = iter(data)

    rules = {}
    for line in it:
        if not line:
            break
        rule_name, _, rule = line.partition(": ")

        options = rule.split(" | ")

        rules[rule_name] = [option.split() for option in options]

    strings = list(it)

    return rules, strings


def resolve_rule(rules, rule_id: str):
    if rule_id.startswith('"'):
        # Not really a rule id, it's a literal
        return rule_id[1:-1]

    options = rules[rule_id]

    return (
        "("
        + "|".join(
            "".join(resolve_rule(rules, r) for r in option) for option in options
        )
        + ")"
    )


def part1(data) -> int:
    rules, strings = data
    matches = 0
    r = re.compile(resolve_rule(rules, "0"))
    for string in strings:
        if r.fullmatch(string):
            matches += 1
    return matches


def part2(data) -> int:
    rules, strings = data
    rule_42 = resolve_rule(rules, "42")
    rule_31 = resolve_rule(rules, "31")

    # 0 -> 8 11
    # 8 -> 42 | 42 8
    # 11 -> 42 31 | 42 11 31

    # 8 is like 42+
    # 11 is like 42{n} 31{n}    ...but you can't do this with regexes.

    # yay for brute force
    regexes = [
        re.compile(f"({rule_42})+({rule_42}){{{n}}}({rule_31}){{{n}}}")
        for n in range(1, 50)
    ]

    matches = 0
    for s in strings:
        for r in regexes:
            if r.fullmatch(s):
                matches += 1
                break

    return matches
