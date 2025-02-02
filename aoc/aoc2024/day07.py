import itertools

type Data = list[tuple[int, list[int]]]


def parse_data(data: list[str]) -> Data:
    parsed = []
    for line in data:
        total, rest = line.split(":")
        operands = [int(i) for i in rest.split()]
        parsed.append((int(total), operands))
    return parsed


def has_valid_solution(total: int, operands: list[int], operators: str) -> bool:
    for operators_ in itertools.product(operators, repeat=len(operands) - 1):
        rt = operands[0]
        for operator, operand in zip(operators_, operands[1:]):
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


def part1(data: Data) -> int:
    return sum(
        total for total, operands in data if has_valid_solution(total, operands, "+*")
    )


def part2(data: Data) -> int:
    return sum(
        total for total, operands in data if has_valid_solution(total, operands, "+*|")
    )
