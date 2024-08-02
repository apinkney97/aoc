import itertools

from aoc import utils


def _parse_data(data):
    data = utils.parse_data(data, fn=lambda line: [int(c) for c in line])

    return data


def p(data):
    for row in data:
        print("".join(str(i) for i in row))


def run(data, max_step=None, flash_threshold=None):
    total_flashes = 0
    for step in itertools.count():
        will_flash = set()
        for x, y in itertools.product(range(10), range(10)):
            data[x][y] += 1
            if data[x][y] > 9:
                will_flash.add((x, y))
        flash_queue = list(will_flash)
        while flash_queue:
            x, y = flash_queue.pop()
            for nx, ny in utils.neighbours((x, y), include_diagonals=True):
                if not ((0 <= nx < 10) and (0 <= ny < 10)):
                    continue
                data[nx][ny] += 1
                if data[nx][ny] > 9 and (nx, ny) not in will_flash:
                    will_flash.add((nx, ny))
                    flash_queue.append((nx, ny))

        for x, y in will_flash:
            data[x][y] = 0

        total_flashes += len(will_flash)

        if step == max_step:
            return total_flashes

        if len(will_flash) == flash_threshold:
            return step + 1


def part1(data) -> int:
    return run(_parse_data(data), max_step=99)


def part2(data) -> int:
    return run(_parse_data(data), flash_threshold=100)
