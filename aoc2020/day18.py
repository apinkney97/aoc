import utils

DATA = utils.load_data(18)


def split(expr):
    expr = expr.replace("(", " ( ")
    expr = expr.replace(")", " ) ")
    return expr.split()


def evaluate(postfix):

    stack = []
    for c in postfix:
        if isinstance(c, int):
            stack.append(c)
        elif c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "*":
            stack.append(stack.pop() * stack.pop())

    if len(stack) != 1:
        raise Exception(f"Expected stack to have length 1; stack was {stack}")

    return stack[0]


def to_postfix(expr, plus_has_precedence=False):

    tokens = split(expr)

    postfix = []
    ops = []

    for t in tokens:
        if t.isnumeric():
            postfix.append(int(t))
        elif t == ")":
            while ops[-1] != "(":
                postfix.append(ops.pop())
            ops.pop()
        else:
            if t != "(":
                while (
                    ops
                    and ops[-1] != "("
                    and (not plus_has_precedence or (t == "*" and ops[-1] == "+"))
                ):
                    postfix.append(ops.pop())
            ops.append(t)

    postfix.extend(reversed(ops))

    return postfix


def part1() -> int:
    return sum(evaluate(to_postfix(expr)) for expr in DATA)


def part2() -> int:
    return sum(evaluate(to_postfix(expr, plus_has_precedence=True)) for expr in DATA)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
