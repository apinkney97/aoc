from aoc.utils import PQ


def test_len() -> None:
    pq = PQ()
    assert len(pq) == 0

    pq.add_item(1)
    pq.add_item(2)

    assert len(pq) == 2

    pq.remove_item(1)
    assert len(pq) == 1


def test_priority():
    pq = PQ()

    numbers = [0, 2, 4, 6, 8, 9, 7, 5, 3, 1]
    for num in numbers:
        pq.add_item(num, priority=num)

    out_numbers = []
    while pq:
        out_numbers.append(pq.pop_item())

    assert out_numbers == sorted(numbers)


def test_priority_max():
    pq = PQ(max_heap=True)

    numbers = [0, 2, 4, 6, 8, 9, 7, 5, 3, 1]
    for num in numbers:
        pq.add_item(num, priority=num)

    out_numbers = []
    while pq:
        out_numbers.append(pq.pop_item())

    assert out_numbers == sorted(numbers, reverse=True)
