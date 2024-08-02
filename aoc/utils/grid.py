from __future__ import annotations

from collections.abc import MutableMapping
from typing import Iterator, TypeVar

from aoc.utils.output import BACKGROUND_BLOCK, FOREGROUND_BLOCK

DEFAULT_DISPLAY_MAP = {
    0: BACKGROUND_BLOCK,
    1: FOREGROUND_BLOCK,
}


KT = TypeVar("KT")
VT = TypeVar("VT")

Coord2D = tuple[int, int]
Coord3D = tuple[int, int, int]


class Grid(MutableMapping[KT, VT]):
    def __init__(self, default_val: VT):
        self._default_val = default_val
        self._grid: dict[KT, VT] = {}

    def __setitem__(self, key: KT, value: VT) -> None:
        if value == self._default_val:
            self._grid.pop(key, None)
        else:
            self._grid[key] = value

    def __getitem__(self, key: KT) -> VT:
        return self._grid.get(key, self._default_val)

    def __delitem__(self, key: KT) -> None:
        self._grid.pop(key)

    def __iter__(self) -> Iterator[KT]:
        return iter(self._grid)

    def __len__(self) -> int:
        return len(self._grid)


class Grid2D(Grid[Coord2D, int]):
    def __init__(
        self,
        default_val: int = 0,
        display_map: dict[int, str] | None = None,
        bounds: tuple[int, int, int, int] | None = None,
    ) -> None:
        super().__init__(default_val=default_val)

        self.max_x: int = 0
        self.max_y: int = 0
        self.min_x: int = 0
        self.min_y: int = 0

        self._display_map = display_map
        if self._display_map is None:
            self._display_map = DEFAULT_DISPLAY_MAP

        # lower bounds inclusive, upper bounds exclusive
        self._bounds = bounds

    def __setitem__(self, key: Coord2D, value: int) -> None:
        if self._bounds:
            x, y = key
            xmin, xmax, ymin, ymax = self._bounds
            if x < xmin or x >= xmax or y < ymin or y >= ymax:
                # Silently ignore
                return

        super().__setitem__(key, value)

        self.max_x = max(self.max_x, key[0])
        self.max_y = max(self.max_y, key[1])
        self.min_x = min(self.min_x, key[0])
        self.min_y = min(self.min_y, key[1])

    def __str__(self) -> str:
        lines = []
        if self._bounds:
            min_x, max_x, min_y, max_y = self._bounds
        else:
            min_x = self.min_x
            max_x = self.max_x + 1
            min_y = self.min_y
            max_y = self.max_y + 1

        for y in range(min_y, max_y):
            line = []
            for x in range(min_x, max_x):
                val = self[x, y]
                if self._display_map:
                    line.append(self._display_map[val])
                else:
                    line.append(str(val))
            lines.append("".join(line))
        return "\n".join(lines)

    def blank_copy(self) -> Grid2D:
        """Returns a new, empty instance with the same config as this instance."""
        return Grid2D(
            default_val=self._default_val,
            display_map=self._display_map,
            bounds=self._bounds,
        )


class Grid3D(Grid[Coord3D, int]):
    pass
