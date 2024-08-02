"""
A: rock, 1, X
B: paper, 2, Y
C: scissors, 3, Z

0 lose
3 draw
6 win
"""

LOSE = 0
DRAW = 3
WIN = 6

ROCK = 1
PAPER = 2
SCISSORS = 3


def part1(data) -> int:
    scores = {
        "A X": ROCK + DRAW,
        "B X": ROCK + LOSE,
        "C X": ROCK + WIN,
        "A Y": PAPER + WIN,
        "B Y": PAPER + DRAW,
        "C Y": PAPER + LOSE,
        "A Z": SCISSORS + LOSE,
        "B Z": SCISSORS + WIN,
        "C Z": SCISSORS + DRAW,
    }
    return sum(scores[row] for row in data)


def part2(data) -> int:
    # X: lose
    # Y: draw
    # Z: win
    scores = {
        "A X": SCISSORS + LOSE,
        "B X": ROCK + LOSE,
        "C X": PAPER + LOSE,
        "A Y": ROCK + DRAW,
        "B Y": PAPER + DRAW,
        "C Y": SCISSORS + DRAW,
        "A Z": PAPER + WIN,
        "B Z": SCISSORS + WIN,
        "C Z": ROCK + WIN,
    }
    return sum(scores[row] for row in data)
