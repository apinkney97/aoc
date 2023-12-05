from aoc2019 import utils


def fuel_needed(mass: int) -> int:
    return max(mass // 3 - 2, 0)


def part1() -> int:
    total_fuel_mass = 0

    for module_mass in utils.load_data(2019, 1):
        module_mass = int(module_mass)
        total_fuel_mass += fuel_needed(module_mass)

    return total_fuel_mass


def part2() -> int:
    total_fuel_mass = 0

    for module_mass in utils.load_data(2019, 1):
        module_mass = int(module_mass)
        extra_fuel_mass = fuel_needed(module_mass)
        total_fuel_mass += extra_fuel_mass

        while extra_fuel_mass := fuel_needed(extra_fuel_mass):
            total_fuel_mass += extra_fuel_mass

    return total_fuel_mass


def main() -> None:
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    main()
