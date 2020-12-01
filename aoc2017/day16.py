import string

from aoc2017.util import load_data

MOVES = []


def dance(progs):
    if not MOVES:
        for move in load_data(16)[0].split(","):
            if move[0] == "s":
                MOVES.append(("s", int(move[1:])))
            elif move[0] == "x":
                pos1, pos2 = (int(i) for i in move[1:].split("/"))
                MOVES.append(("x", pos1, pos2))
            elif move[0] == "p":
                prog1, prog2 = move[1:].split("/")
                MOVES.append(("p", prog1, prog2))

    for move in MOVES:
        if move[0] == "s":
            progs = progs[-move[1] :] + progs[: -move[1]]
        elif move[0] == "x":
            pos1, pos2 = move[1:]
            progs[pos1], progs[pos2] = progs[pos2], progs[pos1]
        elif move[0] == "p":
            prog1, prog2 = move[1:]
            pos1 = progs.index(prog1)
            pos2 = progs.index(prog2)
            progs[pos1], progs[pos2] = progs[pos2], progs[pos1]

    return progs


def part1():
    progs = dance(list(string.ascii_lowercase[:16]))
    return "".join(progs)


def part2():
    repeat = 1000000000

    progs = list(string.ascii_lowercase[:16])
    seen = {tuple(progs)}
    seen_list = [progs[:]]

    for _ in range(repeat):
        progs = dance(progs)
        if tuple(progs) in seen:
            break
        seen.add(tuple(progs))
        seen_list.append(progs[:])

    # make sure we're back at the start, and not somewhere else
    assert "".join(progs) == string.ascii_lowercase[:16]

    return "".join(seen_list[repeat % len(seen)])


if __name__ == "__main__":
    print("Part 1: {}".format(part1()))
    print("Part 2: {}".format(part2()))
