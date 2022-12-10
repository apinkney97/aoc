import utils

# EXAMPLE = True
EXAMPLE = False


def load_data():
    data = utils.load_data(10, example=EXAMPLE)

    instructions = []
    for line in data:
        if line != "noop":
            instructions.append("noop")
        instructions.append(line)

    return instructions


DATA = load_data()


def part1() -> int:

    x = 1

    total = 0
    for cycle, instruction in enumerate(DATA, start=1):
        if cycle in {20, 60, 100, 140, 180, 220}:
            total += cycle * x

        if instruction != "noop":
            value = int(instruction.split()[1])
            x += value
    return total


def part2() -> int:
    sprite_x = 1

    for cycle, instruction in enumerate(DATA, start=0):
        if sprite_x - 1 <= cycle % 40 <= sprite_x + 1:
            print("#", end="")
        else:
            print(".", end="")

        if (cycle + 1) % 40 == 0:
            print()

        if instruction != "noop":
            value = int(instruction.split()[1])
            sprite_x += value

    return 0


def main() -> None:
    with utils.timed():
        print(f"Part 1: {part1()}")
    with utils.timed():
        print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
