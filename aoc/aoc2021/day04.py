type Board = list[int]
type Data = tuple[list[int], list[Board]]


def parse_data(data: list[str]) -> Data:
    called_numbers = [int(i) for i in data[0].split(",")]
    boards = []
    board: Board = []

    for line in data[1:]:
        if not line:
            board = []
            boards.append(board)
        board.extend([int(i) for i in line.split()])

    return called_numbers, boards


def part1(data: Data) -> int:
    called_numbers, boards = data
    nums_to_boards: dict[int, list[Board]] = {}
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


def is_winning(board: Board, called: set[int]) -> bool:
    for i in range(5):
        row = board[5 * i : 5 * i + 5]
        if all(num in called for num in row):
            return True
        col = [board[i + n * 5] for n in range(5)]
        if all(num in called for num in col):
            return True

    return False


def part2(data: Data) -> int:
    called_numbers, boards = data
    nums_to_boards: dict[int, list[tuple[int, Board]]] = {}
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
