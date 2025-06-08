type Data = list[str]


def split(expr: str) -> list[str]:
    expr = expr.replace("(", " ( ")
    expr = expr.replace(")", " ) ")
    return expr.split()


def evaluate(postfix: list[str | int]) -> int:
    stack: list[int] = []
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


def to_postfix(expr: str, plus_has_precedence: bool = False) -> list[str | int]:
    tokens = split(expr)

    postfix: list[str | int] = []
    ops: list[str] = []

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


def part1(data: Data) -> int:
    return sum(evaluate(to_postfix(expr)) for expr in data)


def part2(data: Data) -> int:
    return sum(evaluate(to_postfix(expr, plus_has_precedence=True)) for expr in data)
