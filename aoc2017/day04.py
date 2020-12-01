from aoc2017.util import load_data


def contains_dupes(words):
    return len(words) != len(set(words))


def contains_anags(words):
    words = ["".join(sorted(word)) for word in words]
    return contains_dupes(words)


def get_valid_count(invalidation_fn):
    count = 0
    for line in load_data(4):
        words = line.strip().split(" ")
        if not invalidation_fn(words):
            count += 1
    return count


if __name__ == "__main__":
    print("Part 1: {}".format(get_valid_count(contains_dupes)))
    print("Part 2: {}".format(get_valid_count(contains_anags)))
