from statistics import median

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


def part1(data) -> int:
    score = 0
    for line in data:
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


def part2(data) -> int:
    scores = []
    for line in data:
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
