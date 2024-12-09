import heapq
from collections import defaultdict, deque
from typing import NamedTuple


class FilePart(NamedTuple):
    start: int
    length: int
    id: int

    @property
    def next(self):
        return self.start + self.length


def parse_data(data):
    files = []
    pos = 0

    for i, char in enumerate(data[0]):
        if i % 2 == 0:
            files.append(FilePart(start=pos, length=int(char), id=i // 2))
            pos += files[-1].length
        else:
            pos += int(char)
    return files


def part1(data) -> int:
    files: deque[FilePart] = deque(data)
    defragged_files = [files.popleft()]

    # If no gap, take whole file from left
    # If gap, fill it from rightmost file, splitting if necessary
    while files:
        next_start = defragged_files[-1].next
        gap = files[0].start - next_start
        if not gap:
            defragged_files.append(files.popleft())
        else:
            if files[-1].length <= gap:
                defragged_files.append(files.pop()._replace(start=next_start))
            else:
                old_file = files.pop()
                defragged_files.append(old_file._replace(start=next_start, length=gap))
                files.append(old_file._replace(length=old_file.length - gap))

    result = 0
    for f in defragged_files:
        for i in range(f.start, f.next):
            result += i * f.id
    return result


def part2(data: list[FilePart]) -> int:
    gaps = defaultdict(list)

    for file1, file2 in zip(data, data[1:]):
        gap = file2.start - file1.next
        if gap:
            heapq.heappush(gaps[gap], file1.next)

    defragged_files = {file.id: file for file in data}
    for file in sorted(data, reverse=True, key=lambda f: f.id):
        available_gaps = sorted(
            (gaps[gap][0], gap)
            for gap in gaps
            if gap >= file.length and gaps[gap][0] < file.start
        )

        if available_gaps:
            gap_pos, gap = available_gaps[0]

            defragged_files[file.id] = file._replace(start=gap_pos)
            heapq.heappop(gaps[gap])

            if not gaps[gap]:
                gaps.pop(gap)

            remaining_gap = gap - file.length
            if remaining_gap:
                heapq.heappush(gaps[remaining_gap], gap_pos + file.length)

    result = 0

    for f in defragged_files.values():
        for i in range(f.start, f.next):
            result += i * f.id
    return result
