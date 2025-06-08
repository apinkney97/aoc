import re
from itertools import chain
from typing import NamedTuple


class Data(NamedTuple):
    fields: dict[str, set[int]]
    my_ticket: list[int]
    tickets: list[list[int]]


def parse_data(data: list[str]) -> Data:
    di = iter(data)

    field_re = re.compile(
        r"(?P<name>[^:]+): (?P<a>\d+)-(?P<b>\d+) or (?P<c>\d+)-(?P<d>\d+)"
    )
    fields = {}
    for line in di:
        if not line:
            break
        match = field_re.fullmatch(line)
        assert match is not None
        values = set(
            chain(
                range(int(match["a"]), int(match["b"]) + 1),
                range(int(match["c"]), int(match["d"]) + 1),
            )
        )
        fields[match["name"]] = values

    next(di)

    def _parse_ticket(ticket: str) -> list[int]:
        return [int(i) for i in ticket.split(",")]

    my_ticket = _parse_ticket(next(di))

    next(di)
    next(di)
    tickets = []

    for line in di:
        tickets.append(_parse_ticket(line))

    return Data(fields=fields, my_ticket=my_ticket, tickets=tickets)


def part1(data: Data) -> int:
    invalid_sum = 0
    for ticket in data.tickets:
        for val in ticket:
            if not any(val in allowed for allowed in data.fields.values()):
                invalid_sum += val

    return invalid_sum


def part2(data: Data) -> int:
    collected_values: list[set[int]] = [set() for _ in range(len(data.tickets[0]))]

    for ticket in data.tickets:
        for val in ticket:
            if not any(val in allowed for allowed in data.fields.values()):
                break

        else:
            for s, val in zip(collected_values, ticket):
                s.add(val)

    values_by_field: dict[int, set[int]] = {
        i: val for i, val in enumerate(collected_values)
    }

    matched = {}
    fields = dict(data.fields)
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

    res = 1
    for field_name, pos in matched.items():
        if field_name.startswith("departure"):
            res *= data.my_ticket[pos]

    return res
