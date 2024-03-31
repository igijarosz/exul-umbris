from typing import Tuple
import numpy as np

graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"),
        ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", bool),  # True if tile can be walked over
        ("transparent", bool),  # True if tile does not block FOV
        ("dark", graphic_dt),  # Graphics for tile not in FOV
    ]
)


def new_tile(
        *,  # Keyword enforcing
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord("."), (100,100,100), (20,20,20))
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord("#"), (100,100,100), (20,20,20))
)
