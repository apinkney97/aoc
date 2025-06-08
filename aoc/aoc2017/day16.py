import string
from typing import NamedTuple

type Data = list[str]


class Spin(NamedTuple):
    x: int


class Exchange(NamedTuple):
    a: int
    b: int


class Partner(NamedTuple):
    a: str
    b: str


MOVES: list[Spin | Exchange | Partner] = []


def parse_data(data: list[str]) -> Data:
    return data[0].split(",")


def dance(moves: Data, progs: list[str]) -> list[str]:
    if not MOVES:
        for move_ in moves:
            if move_[0] == "s":
                MOVES.append(Spin(int(move_[1:])))
            elif move_[0] == "x":
                pos1, pos2 = (int(i) for i in move_[1:].split("/"))
                MOVES.append(Exchange(pos1, pos2))
            elif move_[0] == "p":
                prog1, prog2 = move_[1:].split("/")
                MOVES.append(Partner(prog1, prog2))

    for move in MOVES:
        if isinstance(move, Spin):
            progs = progs[-move.x :] + progs[: -move.x]
        elif isinstance(move, Exchange):
            progs[move.a], progs[move.b] = progs[move.b], progs[move.a]
        elif isinstance(move, Partner):
            pos1 = progs.index(move.a)
            pos2 = progs.index(move.b)
            progs[pos1], progs[pos2] = progs[pos2], progs[pos1]

    return progs


def part1(data: Data) -> str:
    progs = dance(data, list(string.ascii_lowercase[:16]))
    return "".join(progs)


def part2(data: Data) -> str:
    repeat = 1000000000

    progs = list(string.ascii_lowercase[:16])
    seen = {tuple(progs)}
    seen_list = [progs[:]]

    for _ in range(repeat):
        progs = dance(data, progs)
        if tuple(progs) in seen:
            break
        seen.add(tuple(progs))
        seen_list.append(progs[:])

    # make sure we're back at the start, and not somewhere else
    assert "".join(progs) == string.ascii_lowercase[:16]

    return "".join(seen_list[repeat % len(seen)])
