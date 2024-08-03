def contains_dupes(words):
    return len(words) != len(set(words))


def contains_anags(words):
    words = ["".join(sorted(word)) for word in words]
    return contains_dupes(words)


def get_valid_count(data, invalidation_fn):
    count = 0
    for line in data:
        words = line.strip().split(" ")
        if not invalidation_fn(words):
            count += 1
    return count


def part1(data):
    return get_valid_count(data, contains_dupes)


def part2(data):
    return get_valid_count(data, contains_anags)
