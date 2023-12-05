"""
A: rock, 1, X
B: paper, 2, Y
C: scissors, 3, Z

0 lose
3 draw
6 win
"""
import utils

# EXAMPLE = True
EXAMPLE = False


LOSE = 0
DRAW = 3
WIN = 6

ROCK = 1
PAPER = 2
SCISSORS = 3


def load_data():
    data = utils.load_data(2022, 2, example=EXAMPLE)

    return data


DATA = load_data()


def part1() -> int:
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
    return sum(scores[row] for row in DATA)


def part2() -> int:
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
    return sum(scores[row] for row in DATA)


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
