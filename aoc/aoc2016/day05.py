from hashlib import md5
from itertools import count

type Data = str


def parse_data(data: list[str]) -> Data:
    return data[0]


def part1(data: Data) -> str:
    chars = []
    for i in count():
        hash_val = md5(f"{data}{i}".encode()).hexdigest()
        if hash_val.startswith("00000"):
            chars.append(hash_val[5])
            if len(chars) == 8:
                break
    return "".join(chars)


def part2(data: Data) -> str:
    chars = [""] * 8
    for i in count():
        hash_val = md5(f"{data}{i}".encode()).hexdigest()
        if hash_val.startswith("00000"):
            pos = hash_val[5]
            if pos in "01234567":
                pos_ = int(pos)
                if chars[pos_] == "":
                    chars[pos_] = hash_val[6]
                    if "" not in chars:
                        break
    return "".join(chars)
