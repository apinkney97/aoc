from aoc import utils

DATA = utils.load_data(2015, 8)


def part1() -> int:
    sum_code = 0
    sum_mem = 0
    for line in DATA:
        sum_code += len(line)
        sum_mem += len(eval(line))

    return sum_code - sum_mem


def part2() -> int:
    sum_code = 0
    sum_escaped = 0
    for line in DATA:
        sum_code += len(line)
        escaped = '"' + line.replace("\\", "\\\\").replace('"', '\\"') + '"'
        sum_escaped += len(escaped)
    return sum_escaped - sum_code


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
