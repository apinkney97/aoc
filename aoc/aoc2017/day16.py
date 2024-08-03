import string

MOVES = []


def parse_data(data):
    return data[0].split(",")


def dance(moves, progs):
    if not MOVES:
        for move in moves:
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


def part1(data):
    progs = dance(data, list(string.ascii_lowercase[:16]))
    return "".join(progs)


def part2(data):
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
