# from collections.abc import MutableMapping
# from typing import TypeVar
#
# KT = TypeVar("KT")
# VT = TypeVar("VT")
#
# Coord2D = tuple[int, int]
# Coord3D = tuple[int, int, int]
#
#
# class Grid(MutableMapping[KT, VT]):
#     def __init__(self, default_val: VT):
#         self._default_val = default_val
#         self._grid: dict[KT, VT] = {}
#
#     def __setitem__(self, key: KT, value: VT) -> None:
#         if value == self._default_val:
#             self._grid.pop(key, None)
#         else:
#             self._grid[key] = value
#
#     def __getitem__(self, key: KT) -> VT:
#         return self._grid.get(key, self._default_val)
#
#     def __delitem__(self, key: KT) -> None:
#         self._grid.pop(key)
#
#     def __iter__(self):
#         return iter(self._grid)
#
#     def __len__(self):
#         return len(self._grid)
#
#
# class Grid2D(Grid[Coord2D, int]):
#     pass
#
#
# class Grid3D(Grid[Coord3D, int]):
#     pass
