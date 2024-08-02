def fuel_needed(mass: int) -> int:
    return max(mass // 3 - 2, 0)


def part1(data) -> int:
    total_fuel_mass = 0

    for module_mass in data:
        module_mass = int(module_mass)
        total_fuel_mass += fuel_needed(module_mass)

    return total_fuel_mass


def part2(data) -> int:
    total_fuel_mass = 0

    for module_mass in data:
        module_mass = int(module_mass)
        extra_fuel_mass = fuel_needed(module_mass)
        total_fuel_mass += extra_fuel_mass

        while extra_fuel_mass := fuel_needed(extra_fuel_mass):
            total_fuel_mass += extra_fuel_mass

    return total_fuel_mass
