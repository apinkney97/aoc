import functools
import operator

from aoc.utils import split_by_blank_lines, transpose


def parse_data(data):
    return split_by_blank_lines(data)


def find_reflection_indices(line: str) -> list[int]:
    reflection_indices = []

    for i in range(1, len(line)):
        start = line[:i]
        end = line[i:]
        pattern_len = min(len(start), len(end))
        start = start[-pattern_len:]
        end = end[:pattern_len]
        end = end[::-1]
        if start == end:
            reflection_indices.append(i)

    return reflection_indices


def find_smudgy_reflection_indices(line: str) -> set[int]:
    # For the given line, returns indices that reflect with one smudge
    smudge_indices = set()
    for i, c in enumerate(line):
        c = "." if c == "#" else "#"
        smudged_line = line[:i] + c + line[i + 1 :]
        smudge_indices.update(find_reflection_indices(smudged_line))
    return smudge_indices


def find_common_reflection_indices(pattern: list[str]) -> dict[int, set[int]]:
    reflections_per_line = {}
    for i, line in enumerate(pattern):
        reflection_indices = find_reflection_indices(line)
        reflections_per_line[i] = set(reflection_indices)

    return reflections_per_line


def part1(data) -> int:
    result = 0
    for pattern in data:
        # Check horizontal slices
        horizontal_indices_per_line = find_common_reflection_indices(pattern)
        horizontal_indices = functools.reduce(
            operator.and_, horizontal_indices_per_line.values()
        )

        if horizontal_indices:
            result += horizontal_indices.pop()
        else:
            vertical_indices_per_line = find_common_reflection_indices(
                transpose(pattern)
            )
            vertical_indices = functools.reduce(
                operator.and_, vertical_indices_per_line.values()
            )
            result += 100 * vertical_indices.pop()

    return result


def find_smudged_reflections(pattern: list[str]) -> int | None:
    indices_per_line = find_common_reflection_indices(pattern)
    lines_per_index = {}
    for line, refl_indices in indices_per_line.items():
        for refl_index in refl_indices:
            lines_per_index.setdefault(refl_index, []).append(line)

    for refl_index, lines in lines_per_index.items():
        lines = set(lines)
        missing_lines = set(indices_per_line) - lines

        if len(missing_lines) == 1:
            missing_line = missing_lines.pop()
            # Candidate for fix-by-desmudging.
            # Check for a smudged line matching this missing line with the same reflection index
            smudgy_reflection_indices = find_smudgy_reflection_indices(
                pattern[missing_line]
            )
            if refl_index in smudgy_reflection_indices:
                return refl_index
    return None


def part2(data) -> int:
    result = 0
    for pattern in data:
        horizontal_match = find_smudged_reflections(pattern)
        if horizontal_match is not None:
            result += horizontal_match

        else:
            vertical_match = find_smudged_reflections(
                ["".join(line) for line in transpose(pattern)]
            )
            result += 100 * vertical_match

    return result
