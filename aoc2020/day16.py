import re
from itertools import chain
from typing import Dict, List, Set

import utils


def load_data():
    data = utils.load_data(16, example=False)
    di = iter(data)

    field_re = re.compile(
        r"(?P<name>[^:]+): (?P<a>\d+)-(?P<b>\d+) or (?P<c>\d+)-(?P<d>\d+)"
    )
    fields = {}
    for line in di:
        if not line:
            break
        match = field_re.fullmatch(line)
        values = set(
            chain(
                range(int(match["a"]), int(match["b"]) + 1),
                range(int(match["c"]), int(match["d"]) + 1),
            )
        )
        fields[match["name"]] = values

    next(di)

    def _parse_ticket(ticket: str) -> List[int]:
        return [int(i) for i in ticket.split(",")]

    my_ticket = _parse_ticket(next(di))

    next(di)
    next(di)
    tickets = []

    for line in di:
        tickets.append(_parse_ticket(line))

    return {"fields": fields, "my_ticket": my_ticket, "tickets": tickets}


DATA = load_data()


def part1() -> int:
    invalid_sum = 0
    fields = DATA["fields"]
    for ticket in DATA["tickets"]:
        for val in ticket:
            if not any(val in allowed for allowed in fields.values()):
                invalid_sum += val

    return invalid_sum


def part2() -> int:
    fields = DATA["fields"]

    collected_values = [set() for _ in range(len(DATA["tickets"][0]))]

    for ticket in DATA["tickets"]:
        for val in ticket:
            if not any(val in allowed for allowed in fields.values()):
                break

        else:
            for s, val in zip(collected_values, ticket):
                s.add(val)

    values_by_field: Dict[int, Set[int]] = {
        i: val for i, val in enumerate(collected_values)
    }

    matched = {}
    fields = dict(fields)
    # Go through each set of values; if it can only match one field spec it must be that one
    while fields:
        for i, vals in values_by_field.items():
            matched_name = None
            for name, allowed_vals in fields.items():
                if vals <= allowed_vals:
                    if matched_name is None:
                        matched_name = name
                    else:
                        # print("double matched")
                        break
            else:
                if matched_name:
                    # print(f"matched {matched_name!r}")
                    fields.pop(matched_name)
                    matched[matched_name] = i

    print(matched)

    my_ticket = DATA["my_ticket"]
    res = 1
    for field_name, pos in matched.items():
        if field_name.startswith("departure"):
            res *= my_ticket[pos]

    return res


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
