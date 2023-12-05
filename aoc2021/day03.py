from collections import Counter

import utils


def load_data():
    data = utils.load_data(2021, 3, example=False)

    return data


DATA = load_data()


def part1() -> int:
    gamma = ""
    epsilon = ""
    for digits in zip(*DATA):
        if digits.count("0") < digits.count("1"):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def part2() -> int:
    def most_common(data, pos):
        c = Counter(d[pos] for d in data)
        return "1" if c["1"] >= c["0"] else "0"

    oxygen = DATA
    for i in range(len(oxygen[0])):
        mc = most_common(oxygen, i)
        oxygen = [d for d in oxygen if d[i] == mc]
        if len(oxygen) == 1:
            break

    co2 = DATA
    for i in range(len(co2[0])):
        mc = most_common(co2, i)
        co2 = [d for d in co2 if d[i] != mc]
        if len(co2) == 1:
            break

    return int(oxygen[0], 2) * int(co2[0], 2)


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
