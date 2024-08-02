def parse_data(data):
    orbits = {}
    inverse_orbits = {}

    for d in data:
        centre, orbiter = d.split(")")
        orbits[orbiter] = centre
        inverse_orbits.setdefault(centre, []).append(orbiter)

    return orbits, inverse_orbits


def count_orbits(inverse_orbits, node, depth) -> int:
    return depth + sum(
        count_orbits(inverse_orbits, k, depth + 1) for k in inverse_orbits.get(node, [])
    )


def path_to_com(orbits, node):
    path = []
    while node != "COM":
        node = orbits[node]
        path.append(node)
    return path


def part1(data) -> int:
    orbits, inverse_orbits = data

    return count_orbits(inverse_orbits, "COM", 0)


def part2(data) -> int:
    orbits, inverse_orbits = data

    you_to_com = path_to_com(orbits, "YOU")
    san_to_com = path_to_com(orbits, "SAN")

    while you_to_com[-1] == san_to_com[-1]:
        you_to_com.pop()
        san_to_com.pop()

    return len(you_to_com) + len(san_to_com)
