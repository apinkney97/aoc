import pathlib
from typing import Callable, Optional

import requests

from aoc.utils.types import T


def load_data(
    year: int,
    day: int,
    strip: bool = True,
    *,
    fn: Optional[Callable[[str], T]] = None,
    example: bool = False,
) -> list[T] | list[str]:
    suffix = "-example" if example else ""
    path = pathlib.Path("aoc") / f"aoc{year}" / "data" / f"day{day:02d}{suffix}.data"

    if not example and (not path.exists() or path.stat().st_size == 0):
        data = _fetch_data(year, day)
        path.write_text(data)

    with open(path) as f:
        data = f.readlines()
        if strip:
            data = [line.strip() for line in data]
        if fn is not None:
            data = [fn(line) for line in data]
        return data


def _get_cookie(force_refresh: bool = False):
    cache_dir = pathlib.Path.home() / ".cache" / "aoc"
    cache_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    cookie = cache_dir / "cookie"
    if cookie.exists() and not force_refresh:
        cookie_value = cookie.read_text()
    else:
        cookie_value = input("Enter cookie: ")
        cookie.write_text(cookie_value)
    return cookie_value.strip()


def _fetch_data(year: int, day: int) -> str:
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
