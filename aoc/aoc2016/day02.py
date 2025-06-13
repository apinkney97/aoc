type Data = list[str]


def parse_data(data: list[str]) -> Data:
    return data


class SquareKeypad:
    def __init__(self) -> None:
        self.x = 1
        self.y = 1

    @property
    def button(self) -> str:
        return str(1 + 3 * self.y + self.x)

    def move(self, direction: str) -> None:
        match direction:
            case "U":
                self.y -= 1
            case "D":
                self.y += 1
            case "R":
                self.x += 1
            case "L":
                self.x -= 1

        self.x = max(0, min(2, self.x))
        self.y = max(0, min(2, self.y))


class DiamondKeypad:
    def __init__(self) -> None:
        """
            1
          2 3 4
        5 6 7 8 9
          A B C
            D
        """
        self.x = 1
        self.y = 3

        self.keys: list[list[str | None]] = [
            [None] * 7,
            [None] * 3 + ["1"] + [None] * 3,
            [None] * 2 + ["2", "3", "4"] + [None] * 2,
            [None] + ["5", "6", "7", "8", "9"] + [None],
            [None] * 2 + ["A", "B", "C"] + [None] * 2,
            [None] * 3 + ["D"] + [None] * 3,
            [None] * 7,
        ]

    @property
    def button(self) -> str:
        key = self.keys[self.y][self.x]
        assert key is not None
        return key

    def move(self, direction: str) -> None:
        if direction in "UD":
            new_y = self.y + (1 if direction == "D" else -1)
            if self.keys[new_y][self.x] is not None:
                self.y = new_y
        else:
            new_x = self.x + (1 if direction == "R" else -1)
            if self.keys[self.y][new_x] is not None:
                self.x = new_x


def part1(data: Data) -> str:
    output = []

    keypad = SquareKeypad()
    for line in data:
        for c in line:
            keypad.move(c)
        output.append(keypad.button)

    return "".join(output)


def part2(data: Data) -> str:
    output = []
    keypad = DiamondKeypad()
    for line in data:
        for c in line:
            keypad.move(c)
        output.append(keypad.button)

    return "".join(output)
