from typing import NamedTuple

from aoc import utils


class Draw(NamedTuple):
    red: int
    green: int
    blue: int


def parse_data(data):
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    games = []
    for line in data:
        game, desc = line.split(": ")
        game_id = int(game.split()[1])
        draws = desc.split("; ")
        parsed_draws = []
        for draw in draws:
            balls = draw.split(", ")
            r = g = b = 0
            for ball in balls:
                num, colour = ball.split()
                num = int(num)
                if colour == "red":
                    r += num
                elif colour == "green":
                    g += num
                elif colour == "blue":
                    b += num
                else:
                    print(f"Bad colour {colour}")
            parsed_draws.append(Draw(r, g, b))
        games.append((game_id, parsed_draws))

    return games


def part1(data) -> int:
    limit_r = 12
    limit_g = 13
    limit_b = 14
    total = 0
    for game_id, draws in data:
        for draw in draws:
            if draw.red > limit_r or draw.green > limit_g or draw.blue > limit_b:
                break
        else:
            total += game_id
    return total


def part2(data) -> int:
    total = 0
    for game_id, draws in data:
        min_r = min_g = min_b = 0
        for draw in draws:
            min_r = max(min_r, draw.red)
            min_g = max(min_g, draw.green)
            min_b = max(min_b, draw.blue)
        total += utils.product((min_r, min_g, min_b))
    return total
