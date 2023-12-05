from collections import deque
from typing import Deque, Tuple

from aoc import utils


def load_data() -> Tuple[Tuple[int], Tuple[int]]:
    data = utils.load_data(2020, 22, example=False)

    di = iter(data)

    p1_cards = []
    for line in di:
        if not line:
            break
        try:
            p1_cards.append(int(line))
        except ValueError:
            pass

    p2_cards = []
    for line in di:
        if not line:
            break
        try:
            p2_cards.append(int(line))
        except ValueError:
            pass

    return tuple(p1_cards), tuple(p2_cards)


DATA = load_data()


def part1() -> int:
    p1 = deque(DATA[0])
    p2 = deque(DATA[1])

    while p1 and p2:
        p1_card = p1.popleft()
        p2_card = p2.popleft()
        round_winner = p1 if p1_card > p2_card else p2
        round_winner.extend(sorted((p1_card, p2_card), reverse=True))

    game_winner = p1 if p1 else p2
    score = 0
    for i, card in enumerate(reversed(game_winner), start=1):
        score += i * card

    return score


GAME = 0


def recursive_combat(p1: Deque[int], p2: Deque[int]) -> int:
    global GAME
    GAME += 1
    this_game = GAME
    seen_states = set()
    utils.log(f"=== Game {GAME} ===\n")

    round_num = 0
    while p1 and p2:
        round_num += 1
        utils.log(f"-- Round {round_num} (Game {this_game}) --")

        utils.log(f"Player 1's deck: {', '.join(str(i) for i in p1)}")
        utils.log(f"Player 2's deck: {', '.join(str(i) for i in p2)}")

        state = tuple(p1), tuple(p2)
        if state in seen_states:
            utils.log("Seen this before! Player 1 wins")
            return 1

        seen_states.add(state)

        p1_card = p1.popleft()
        p2_card = p2.popleft()

        utils.log(f"Player 1 plays: {p1_card}")
        utils.log(f"Player 2 plays: {p2_card}")

        if len(p1) >= p1_card and len(p2) >= p2_card:
            utils.log("Playing a sub-game to determine the winner...\n")
            p1_copy = deque(list(p1)[:p1_card])
            p2_copy = deque(list(p2)[:p2_card])
            round_winner = recursive_combat(p1_copy, p2_copy)
            utils.log(f"...anyway, back to game {this_game}.")

        else:
            round_winner = 1 if p1_card > p2_card else 2

        utils.log(
            f"Player {round_winner} wins round {round_num} of game {this_game}!\n"
        )

        if round_winner == 1:
            p1.append(p1_card)
            p1.append(p2_card)
        else:
            p2.append(p2_card)
            p2.append(p1_card)

    game_winner = 1 if p1 else 2
    utils.log(f"The winner of game {this_game} is player {game_winner}!\n")

    return game_winner


def part2() -> int:
    p1 = deque(DATA[0])
    p2 = deque(DATA[1])

    recursive_combat(p1, p2)

    game_winner = p1 if p1 else p2
    score = 0
    for i, card in enumerate(reversed(game_winner), start=1):
        score += i * card

    return score


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
