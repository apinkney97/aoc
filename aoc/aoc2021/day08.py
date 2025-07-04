type Data = list[tuple[list[set[str]], list[set[str]]]]


def parse_data(data: list[str]) -> Data:
    parsed_data = []
    for row in data:
        sample_digits_raw, output_raw = row.split("|")
        sample_digits = [set(d) for d in sample_digits_raw.split()]
        output = [set(d) for d in output_raw.split()]
        parsed_data.append((sample_digits, output))

    return parsed_data


DIGITS = {
    0: set("abcefg"),
    1: set("cf"),
    2: set("acdeg"),
    3: set("acdfg"),
    4: set("bcdf"),
    5: set("abdfg"),
    6: set("abdefg"),
    7: set("acf"),
    8: set("abcdefg"),
    9: set("abcdfg"),
}


def part1(data: Data) -> int:
    count = 0
    for _, output in data:
        for digit in output:
            if len(digit) in (2, 4, 3, 7):
                count += 1
    return count


def part2(data: Data) -> int:
    total = 0

    for sample_digits, output in data:
        # We know 1, 4, 7, 8
        known_digits = {}

        # 0, 6, 9 are missing 1 segment
        # 2, 3, 5 are missing 2 segments
        zero_six_nine = []
        two_three_five = []

        segments_to_digits: dict[str, list[set[str]]] = {}

        for digit in sample_digits:
            for segment in digit:
                segments_to_digits.setdefault(segment, []).append(digit)

            if len(digit) == 2:
                known_digits[1] = digit
            elif len(digit) == 4:
                known_digits[4] = digit
            elif len(digit) == 3:
                known_digits[7] = digit
            elif len(digit) == 7:
                known_digits[8] = digit
            elif len(digit) == 6:
                zero_six_nine.append(digit)
            elif len(digit) == 5:
                two_three_five.append(digit)

        #  we can identify number 2, because of all digits it's the only one missing segment 'f'
        for segment, ds in segments_to_digits.items():
            if (len(ds)) == 9:
                known_digits[2] = [d for d in sample_digits if d not in ds][0]

        for digit in two_three_five:
            common_segments = digit & known_digits[2]
            if len(common_segments) == 3:
                # 5 has 3 segments in common with 2
                known_digits[5] = digit
            elif len(common_segments) == 4:
                # 3 has 4 segments in common with 2
                known_digits[3] = digit

        for digit in zero_six_nine:
            if len(digit & known_digits[1]) == 1:
                # 6 has 1 in common with 1
                known_digits[6] = digit
            elif len(digit & known_digits[5]) == 5:
                # 9 has 5 in common with 5
                known_digits[9] = digit
            else:
                # The other one must be 0
                known_digits[0] = digit

        flattened_digits = {}
        for digit_num, segments in known_digits.items():
            flattened_digits["".join(sorted(segments))] = digit_num
            pass

        n = 0
        for digit in output:
            n *= 10
            digit_str = "".join(sorted(digit))
            n += flattened_digits[digit_str]

        total += n

    return total
