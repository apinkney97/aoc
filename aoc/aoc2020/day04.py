import re

HCL_RE = re.compile(r"^#[0-9a-f]{6}$")


FIELDS = {
    "byr": "Birth Year",
    "iyr": "Issue Year",
    "eyr": "Expiration Year",
    "hgt": "Height",
    "hcl": "Hair Color",
    "ecl": "Eye Color",
    "pid": "Passport ID",
    "cid": "Country ID",
}


def parse_data(data):
    parsed = []
    passport = {}
    for line in data:
        if not line:
            parsed.append(passport)
            passport = {}
            continue
        for field in line.split():
            key, _, val = field.partition(":")
            passport[key] = val

    return parsed


def part1(data) -> int:
    valid = 0
    for passport in data:
        missing = FIELDS.keys() - passport.keys()
        if not missing or missing == {"cid"}:
            valid += 1

    return valid


def part2(data) -> int:
    valid = 0
    for passport in data:
        if not 1920 <= int(passport.get("byr", 0)) <= 2002:
            continue

        if not 2010 <= int(passport.get("iyr", 0)) <= 2020:
            continue

        if not 2020 <= int(passport.get("eyr", 0)) <= 2030:
            continue

        hgt = passport.get("hgt", "")
        if hgt.endswith("cm"):
            if not 150 <= int(hgt[:-2]) <= 193:
                continue
        elif hgt.endswith("in"):
            if not 59 <= int(hgt[:-2]) <= 76:
                continue
        else:
            continue

        if not HCL_RE.match(passport.get("hcl", "")):
            continue

        if passport.get("ecl", "") not in {
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth",
        }:
            continue

        pid = passport.get("pid", "")
        if not (len(pid) == 9 and pid.isdigit()):
            continue

        valid += 1
    return valid
