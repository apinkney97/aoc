from aoc import utils


def load_data():
    data = utils.load_data(2021, 4, example=False)

    called_numbers = [int(i) for i in data[0].split(",")]
    boards = []
    board = None

    for line in data[1:]:
        if not line:
            board = []
            boards.append(board)
        board.extend([int(i) for i in line.split()])

    return called_numbers, boards


DATA = load_data()


def part1() -> int:
    called_numbers, boards = DATA
    nums_to_boards = {}
    for board in boards:
        for num in board:
            nums_to_boards.setdefault(num, []).append(board)

    called = set()
    for num in called_numbers:
        called.add(num)
        for board in nums_to_boards.get(num, []):
            if is_winning(board, called):
                unmarked = [n for n in board if n not in called]
                return sum(unmarked) * num

    return -999


def is_winning(board: list[int], called: set[int]) -> bool:
    for i in range(5):
        row = board[5 * i : 5 * i + 5]
        if all(num in called for num in row):
            return True
        col = [board[i + n * 5] for n in range(5)]
        if all(num in called for num in col):
            return True

    return False


def part2() -> int:
    called_numbers, boards = DATA
    nums_to_boards = {}
    for i, board in enumerate(boards):
        for num in board:
            nums_to_boards.setdefault(num, []).append((i, board))

    has_won = set()

    called = set()
    for num in called_numbers:
        called.add(num)
        for i, board in nums_to_boards.get(num, []):
            if i not in has_won and is_winning(board, called):
                has_won.add(i)
                if len(has_won) == len(boards):
                    unmarked = [n for n in board if n not in called]
                    return sum(unmarked) * num

    return -999


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
