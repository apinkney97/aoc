def part1(data) -> int:
    sum_code = 0
    sum_mem = 0
    for line in data:
        sum_code += len(line)
        sum_mem += len(eval(line))

    return sum_code - sum_mem


def part2(data) -> int:
    sum_code = 0
    sum_escaped = 0
    for line in data:
        sum_code += len(line)
        escaped = '"' + line.replace("\\", "\\\\").replace('"', '\\"') + '"'
        sum_escaped += len(escaped)
    return sum_escaped - sum_code
