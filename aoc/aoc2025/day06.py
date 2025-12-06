from aoc import utils

type Data = list[str]


def parse_data(data: list[str]) -> Data:
    return data


def part1(data: Data) -> int:
    transposed = list(zip(*[line.split() for line in data]))
    parsed = [([int(n) for n in col[:-1]], col[-1]) for col in transposed]
    result = 0
    for nums, op in parsed:
        if op == "+":
            result += sum(nums)
        elif op == "*":
            result += utils.product(nums)
    return result


def part2(data: Data) -> int:
    transposed = list(zip(*data))
    op = ""
    problems = []
    nums: list[int] = []
    for line in transposed:
        num = "".join(line[:-1]).strip()
        op = line[-1].strip() or op
        if not num:
            problems.append((nums, op))
            nums = []
            op = ""
        else:
            nums.append(int(num))

    problems.append((nums, op))

    result = 0
    for nums, op in problems:
        if op == "+":
            result += sum(nums)
        elif op == "*":
            result += utils.product(nums)

    return result
