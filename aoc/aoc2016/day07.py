type Data = list[str]


def parse_data(data: list[str]) -> Data:
    return data


def supports_tls(line: str) -> bool:
    brackets = 0
    outside = False
    inside = False
    for offset in range(len(line) - 3):
        chars = line[offset : offset + 4]
        if chars.isalpha():
            if chars[0] == chars[3] and chars[1] == chars[2] and chars[0] != chars[1]:
                if brackets == 0:
                    outside = True
                else:
                    inside = True
        elif chars[0] == "[":
            brackets += 1
        elif chars[0] == "]":
            brackets -= 1

    return outside and not inside


def supports_ssl(line: str) -> bool:
    brackets = 0
    inside = set()
    outside = set()

    for offset in range(len(line) - 2):
        chars = line[offset : offset + 3]
        if chars.isalpha():
            if chars[0] == chars[2] and chars[0] != chars[1]:
                if brackets == 0:
                    outside.add(chars)
                else:
                    inside.add(chars)
        elif chars[0] == "[":
            brackets += 1
        elif chars[0] == "]":
            brackets -= 1

    for pal in outside:
        if f"{pal[1]}{pal[0]}{pal[1]}" in inside:
            return True

    return False


def part1(data: Data) -> int:
    result = 0
    for line in data:
        if supports_tls(line):
            result += 1
    return result


def part2(data: Data) -> int:
    result = 0
    for line in data:
        if supports_ssl(line):
            result += 1
    return result
