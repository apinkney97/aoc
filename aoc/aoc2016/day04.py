import re
from collections import Counter

type Data = list[tuple[str, int, str]]


def parse_data(data: list[str]) -> Data:
    matcher = re.compile(r"^([a-z-]+)-(\d+)\[([a-z]+)]$")
    parsed = []
    for line in data:
        match = matcher.match(line)
        assert match is not None
        parsed.append((match.group(1), int(match.group(2)), match.group(3)))
    return parsed


def generate_checksum(name: str) -> str:
    return "".join(
        letter
        for letter, count in sorted(
            list(Counter(name.replace("-", "")).items()),
            key=lambda item: (-item[1], item[0]),
        )[:5]
    )


def decrypt(name: str, sector: int) -> str:
    letters = []
    for c in name:
        if c == "-":
            letters.append(" ")
        else:
            letters.append(chr((ord(c) - ord("a") + sector) % 26 + ord("a")))
    return "".join(letters)


def part1(data: Data) -> int:
    result = 0
    for name, sector_id, checksum in data:
        if generate_checksum(name) == checksum:
            result += sector_id
    return result


def part2(data: Data) -> int:
    result = 0
    for name, sector_id, checksum in data:
        if generate_checksum(name) == checksum:
            decrypted = decrypt(name, sector_id)
            if "north" in decrypted:
                print(decrypted, sector_id)

    return result
