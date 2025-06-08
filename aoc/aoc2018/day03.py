import re

type Data = list[str]
type Coord = tuple[int, int]

CLAIM_RE = re.compile(
    r"#(?P<claim_id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)"
)


def get_claim(claim_str: str) -> tuple[int, int, int, int, int]:
    claim = CLAIM_RE.match(claim_str)
    assert claim is not None
    claim_id = int(claim.group("claim_id"))
    x = int(claim.group("x"))
    y = int(claim.group("y"))
    w = int(claim.group("w"))
    h = int(claim.group("h"))
    return claim_id, x, y, w, h


def part1(data: Data) -> int:
    taken: set[Coord] = set()
    overlapping: set[Coord] = set()

    for claim in data:
        claim_id, x, y, w, h = get_claim(claim)
        for i in range(x, x + w):
            for j in range(y, y + h):
                coord = (i, j)
                if coord in taken:
                    overlapping.add(coord)
                taken.add(coord)
    return len(overlapping)


def part2(data: Data) -> set[int]:
    claims = [get_claim(claim) for claim in data]

    taken: dict[Coord, int] = {}
    overlapping: set[int] = set()
    claim_ids: set[int] = set()

    for claim in claims:
        claim_id, x, y, w, h = claim
        claim_ids.add(claim_id)
        for i in range(x, x + w):
            for j in range(y, y + h):
                coord = (i, j)

                if coord in taken:
                    overlapping.add(taken[coord])
                    overlapping.add(claim_id)
                else:
                    taken[coord] = claim_id

    return claim_ids - overlapping
