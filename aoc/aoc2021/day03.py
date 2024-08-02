from collections import Counter


def part1(data) -> int:
    gamma = ""
    epsilon = ""
    for digits in zip(*data):
        if digits.count("0") < digits.count("1"):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


def part2(data) -> int:
    def most_common(data, pos):
        c = Counter(d[pos] for d in data)
        return "1" if c["1"] >= c["0"] else "0"

    oxygen = data
    for i in range(len(oxygen[0])):
        mc = most_common(oxygen, i)
        oxygen = [d for d in oxygen if d[i] == mc]
        if len(oxygen) == 1:
            break

    co2 = data
    for i in range(len(co2[0])):
        mc = most_common(co2, i)
        co2 = [d for d in co2 if d[i] != mc]
        if len(co2) == 1:
            break

    return int(oxygen[0], 2) * int(co2[0], 2)
