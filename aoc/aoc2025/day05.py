import collections

type Data = tuple[list[Range], list[int]]


class Range:
    def __init__(self, start: int, end: int) -> None:
        self._start = start  # inclusive
        self._end = end  # exclusive

    @property
    def start(self) -> int:
        return self._start

    @property
    def end(self) -> int:
        return self._end

    def __len__(self) -> int:
        return self.end - self.start

    def __contains__(self, value: int) -> bool:
        return self.start <= value < self.end

    def __repr__(self) -> str:
        return f"Range({self.start}, {self.end})"

    def __eq__(self, other: Range) -> bool:  # type: ignore [override]
        if type(self) is not type(other):
            return NotImplemented
        return self.start == other.start and self.end == other.end

    def __lt__(self, other: Range) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.start < other.start

    def join(self, other: Range) -> Range:
        if not self.overlaps_or_touches(other):
            raise Exception("Can't join")
        return Range(start=min(self.start, other.start), end=max(self.end, other.end))

    def overlaps_or_touches(self, other: Range) -> bool:
        other_in_this = self.start <= other.start <= self.end
        this_in_other = other.start <= self.start <= other.end
        return other_in_this or this_in_other


def parse_data(data: list[str]) -> Data:
    it = iter(data)
    ranges = []
    ids = []
    for line in it:
        if not line:
            break
        start, end = line.split("-")
        ranges.append(Range(int(start), int(end)))

    for line in it:
        ids.append(int(line))

    return ranges, ids


def part1(data: Data) -> int:
    result = 0
    ranges, ids = data

    for id_ in data[1]:
        if any(id_ in r for r in ranges):
            result += 1
    return result


def part2(data: Data) -> int:
    ranges = data[0]

    disjoint_ranges = []

    queue = collections.deque(sorted(ranges))
    curr_r = Range(0, 0)

    while queue:
        next_r = queue.popleft()
        if curr_r.overlaps_or_touches(next_r):
            curr_r = curr_r.join(next_r)
        else:
            disjoint_ranges.append(curr_r)
            curr_r = next_r

    disjoint_ranges.append(curr_r)

    return sum(len(r) for r in disjoint_ranges)
