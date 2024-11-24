def parse_data(data):
    return data[0].split(",")


def hash_(s: str) -> int:
    current = 0

    for c in s:
        current += ord(c)
        current *= 17
        current %= 256

    return current


def part1(data) -> int:
    result = 0
    for item in data:
        result += hash_(item)
    return result


def part2(data) -> int:
    boxes: list[list[tuple[str, int]]] = [[] for _ in range(256)]

    for item in data:
        if item[-1] == "-":
            # Remove the lens with this label (if it exists)
            label_to_remove = item[:-1]
            hash_value = hash_(label_to_remove)
            box = boxes[hash_value]
            for i, (label, _) in enumerate(box):
                if label == label_to_remove:
                    del box[i]
                    break

        else:
            # Add a lens of this focal length with this label
            label_to_add, focal_length = item.split("=")
            focal_length = int(focal_length)
            hash_value = hash_(label_to_add)
            box = boxes[hash_value]
            for i, (label, _) in enumerate(box):
                if label == label_to_add:
                    box[i] = (label_to_add, focal_length)
                    break
            else:
                box.append((label_to_add, focal_length))

    result = 0

    for i, box in enumerate(boxes, start=1):
        for j, (_, focal_length) in enumerate(box, start=1):
            result += i * j * focal_length

    return result
