import re
import string


def parse_data(data):
    return data[0]


VALUE_TO_LETTER = dict(enumerate(string.ascii_lowercase))
LETTER_TO_VALUE = {letter: value for value, letter in VALUE_TO_LETTER.items()}

PAIR_RE = re.compile(r"(.)\1")


def enumerate_lower_str(start: str):
    padding = len(start)
    val = str_to_num(start)
    while True:
        str_val = num_to_str(val, pad_width=padding)
        if len(str_val) > padding:
            val = 0
            padding += 1
            continue
        yield str_val
        val += 1


def str_to_num(s: str) -> int:
    base = len(VALUE_TO_LETTER)
    total = 0
    for i, c in enumerate(s[::-1]):
        total += (base**i) * LETTER_TO_VALUE[c]
    return total


def num_to_str(number: int, pad_width: int = 0) -> str:
    result = _num_to_str(number)
    if len(result) < pad_width:
        result = f"{VALUE_TO_LETTER[0] * (pad_width - len(result))}{result}"

    return result


def _num_to_str(number: int) -> str:
    d, m = divmod(number, 26)
    if d > 0:
        return f"{_num_to_str(d)}{VALUE_TO_LETTER[m]}"
    return VALUE_TO_LETTER[m]


def get_passwords(data):
    for candidate in enumerate_lower_str(data):
        if any(c in candidate for c in "iol"):
            continue
        if len(set(PAIR_RE.findall(candidate))) < 2:
            continue
        for x, y, z in zip(candidate, candidate[1:], candidate[2:]):
            if (ord(x) + 1) == ord(y) == (ord(z) - 1):
                break
        else:
            continue

        yield candidate


def part1(data) -> str:
    return next(get_passwords(data))


def part2(data) -> str:
    gp = get_passwords(data)
    next(gp)
    return next(gp)
