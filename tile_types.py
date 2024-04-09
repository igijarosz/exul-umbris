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
        ("light", graphic_dt),  # Kolor, jeżeli jest w polu widzenia
    ]
)


def new_tile(
        *,  # Keyword enforcing
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD -- jeszcze niezobaczone miejsce
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord("."), (100, 100, 100), (0, 0, 0)),
    light=(ord("."), (200, 200, 200), (0, 0, 0))

)

wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("#"),(100, 100, 100), (0, 0, 0)),
    light=(ord("#"),(200, 200, 200), (0, 0, 0))
)
