import itertools


def parse_data(data):
    parsed = []
    for line in data:
        total, rest = line.split(":")
        total = int(total)
        operands = [int(i) for i in rest.split()]
        parsed.append((total, operands))
    return parsed


def has_valid_solution(total, operands, operators):
    for operators in itertools.product(operators, repeat=len(operands) - 1):
        rt = operands[0]
        for operator, operand in zip(operators, operands[1:]):
            match operator:
                case "+":
                    rt += operand
                case "*":
                    rt *= operand
                case "|":
                    rt = int(f"{rt}{operand}")
        if rt == total:
            return True
    return False


def part1(data) -> int:
    return sum(
        total for total, operands in data if has_valid_solution(total, operands, "+*")
    )


def part2(data) -> int:
    return sum(
        total for total, operands in data if has_valid_solution(total, operands, "+*|")
    )
