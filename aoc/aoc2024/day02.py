def parse_data(data):
    reports = []
    for line in data:
        reports.append([int(i) for i in line.split()])

    return reports


def safe(report: list[int]) -> bool:
    if report[0] < report[1]:
        # check for strictly ascending
        for a, b in zip(report, report[1:]):
            if not 1 <= b - a <= 3:
                return False
        return True
    elif report[0] > report[1]:
        # check for strictly descending
        for a, b in zip(report, report[1:]):
            if not 1 <= a - b <= 3:
                return False
        return True
    return False


def part1(data) -> int:
    result = 0
    for report in data:
        if safe(report):
            result += 1
    return result


def part2(data) -> int:
    result = 0
    for report in data:
        if safe(report):
            result += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1 :]
                if safe(modified_report):
                    result += 1
                    break
    return result
