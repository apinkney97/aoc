import itertools

from aoc import utils


def load_data():
    data = utils.load_data(
        2021, 11, fn=lambda line: [int(c) for c in line], example=False
    )

    return data


def p(data):
    for row in data:
        print("".join(str(i) for i in row))


def run():
    data = load_data()
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

        if step == 99:
            print(f"Part 1: {total_flashes}")

        if len(will_flash) == 100:
            print(f"Part 2: {step + 1}")
            break


def main() -> None:
    run()


if __name__ == "__main__":
    main()
