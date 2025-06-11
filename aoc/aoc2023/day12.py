import re
from collections.abc import Collection, Generator
from functools import cache

Line = tuple[str, tuple[int, ...]]


def parse_data(data: list[str]) -> list[Line]:
    parsed = []
    for line in data:
        template, runs = line.split()
        template = template.replace(".", "_")
        template = template.replace("?", ".")
        parsed_runs = tuple(int(n) for n in runs.split(","))
        parsed.append((template, parsed_runs))
    return parsed


@cache
def split_spaces(slop: int, num_gaps: int) -> Generator[list[int], None, None]:
    # Return all the ways that N spaces can be split across M gaps
    if num_gaps == 1:
        yield [slop]
        return

    for pos in range(slop + 1):
        for subproblem in split_spaces(slop - pos, num_gaps - 1):
            yield [pos, *subproblem]


def to_string(arrangement: list[int], runs: Collection[int]) -> str:
    if len(arrangement) - len(runs) != 1:
        raise ValueError("Arrangement must be exactly 1 longer than runs")
    parts = []
    for spaces, filled in zip(arrangement, runs):
        parts.extend(["_"] * (spaces + 1))
        parts.extend(["#"] * filled)
    parts.extend(["_"] * arrangement[-1])
    return "".join(parts[1:])


def brute_force(template: str, runs: tuple[int, ...]) -> int:
    # Brute force check every possible arrangement
    matching_arrangements = 0
    slop = get_slop(len(template), runs)
    num_gaps = len(runs) + 1

    for arrangement in split_spaces(slop, num_gaps):
        if re.fullmatch(template, to_string(arrangement, runs)):
            matching_arrangements += 1
            # print(to_string(arrangement, runs))

    return matching_arrangements


def part1(data: list[Line]) -> int:
    result = 0
    for template, runs in data:
        matches = brute_force(template, runs)
        result += matches
    return result


@cache
def get_slop(width: int, runs: tuple[int, ...]) -> int:
    return width - sum(n + 1 for n in runs) + 1


@cache
def slide(template: str, runs: tuple[int, ...]) -> int:
    slop = get_slop(len(template), runs)
    matches = 0

    for offset in range(slop + 1):
        # test the first run against the template at every offset

        candidate_parts = ["_"] * offset + ["#"] * runs[0]

        if len(runs) > 1:
            # We only want to match up to the end of this run plus one space
            template_fragment = template[: offset + runs[0] + 1]
            candidate_parts.append("_")
        else:
            # Only one run, so use the full template and pad the candidate with spaces
            template_fragment = template
            candidate_parts.extend(["_"] * (len(template) - len(candidate_parts)))

        if re.fullmatch(template_fragment, "".join(candidate_parts)):
            if len(runs) == 1:
                matches += 1
            else:
                matches += slide(template[len(template_fragment) :], runs[1:])

    return matches


def part2(data: list[Line]) -> int:
    # Brute force we used in part 1 won't work here.
    # Instead, try sliding pieces along in places they could potentially fit,
    # so we can prune unreachable states earlier.

    unfolded_data = []
    for template, runs in data:
        unfolded_data.append((".".join([template] * 5), runs * 5))

    result = 0
    for template, runs in unfolded_data:
        matches = slide(template, runs)
        result += matches
    return result
