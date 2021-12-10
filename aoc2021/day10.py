from statistics import median

import utils


def load_data():
    data = utils.load_data(10, example=False)

    return data


DATA = load_data()

MATCHES = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

BAD_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def part1() -> int:
    score = 0
    for line in DATA:
        stack = []
        for c in line:
            if c in "([{<":
                stack.append(c)
            elif c in MATCHES:
                top = stack.pop()
                if top != MATCHES[c]:
                    score += BAD_SCORES[c]
                    break

    return score


GOOD_SCORES = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def part2() -> int:
    scores = []
    for line in DATA:
        score = 0
        stack = []
        for c in line:
            if c in "([{<":
                stack.append(c)
            elif c in MATCHES:
                top = stack.pop()
                if top != MATCHES[c]:
                    break
        else:
            for c in reversed(stack):
                score = score * 5 + GOOD_SCORES[c]
            scores.append(score)

    return median(scores)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
