from typing import Callable, Optional

import platformdirs
import requests

from aoc.utils.types import T

APP_NAME = "aoc"

# Used for input data
CACHE_PATH = platformdirs.user_cache_path(APP_NAME)

# Used for config data, eg cookie value
CONFIG_PATH = platformdirs.user_config_path(APP_NAME)


def multiline_input(message: str) -> str:
    print(message)
    print("^D to end")
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return "\n".join(lines)


def load_data(
    year: int,
    day: int,
    strip: bool = True,
    *,
    fn: Optional[Callable[[str], T]] = None,
    example: bool = False,
) -> list[T] | list[str]:
    suffix = "-example" if example else ""
    CACHE_PATH.mkdir(mode=0o700, parents=True, exist_ok=True)

    path = CACHE_PATH / f"{year}-{day:02d}{suffix}.txt"

    print("Input path:", path)

    if not path.exists() or path.stat().st_size == 0:
        if example:
            data = multiline_input(f"Paste example data for day {day} {year}")

        else:
            data = _fetch_input_data(year, day)

        path.write_text(data)

    with open(path) as f:
        data = f.readlines()
        if strip:
            data = [line.strip() for line in data]
        if fn is not None:
            data = [fn(line) for line in data]
        return data


def _get_cookie(force_refresh: bool = False):
    CONFIG_PATH.mkdir(mode=0o700, parents=True, exist_ok=True)
    cookie = CONFIG_PATH / "cookie"
    print("Cookie path:", cookie)
    if cookie.exists() and not force_refresh:
        cookie_value = cookie.read_text()
    else:
        cookie_value = input("Enter value of `session` cookie: ")
        cookie.write_text(cookie_value)
    return cookie_value.strip()


def _fetch_input_data(year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    print(f"About to fetch {url}")
    headers = {
        "User-Agent": "github.com/apinkney97/aoc/ by apinkney97<at>gmail<dot>com",
    }
    resp = requests.get(url, headers=headers, cookies={"session": _get_cookie()})

    if resp.status_code != 200:
        # Try again after refreshing the cookie
        resp = requests.get(
            url, headers=headers, cookies={"session": _get_cookie(force_refresh=True)}
        )

    if resp.status_code != 200:
        raise Exception(
            f"Couldn't get input. Bad cookie? {resp.status_code = } {resp.text = }"
        )

    return resp.text
