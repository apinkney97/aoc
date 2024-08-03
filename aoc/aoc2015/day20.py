def parse_data(data):
    return int(data[0])


def factorise(number: int) -> set[int]:
    factors = {1, number}
    for i in range(2, int(number**0.5 + 1)):
        if not number % i:
            factors.add(i)
            factors.add(number // i)

    return factors


def part1(data) -> int:
    for house in range(1, 1000000):
        presents = 10 * sum(factorise(house))
        if presents >= data:
            return house
    return -1


def part2(data) -> int:
    for house in range(1, 1000000):
        presents = 11 * sum(
            factor for factor in factorise(house) if house <= factor * 50
        )
        if presents >= data:
            return house

    return -1
