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
        ("walkable", bool),  # True, jeśli da się poruszać
        ("transparent", bool),  # True, jeśli nie blokuje pola widzenia
        ("dark", graphic_dt),  # Kolor, jeżeli nie jest w polu widzenia
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
