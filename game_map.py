import numpy as np
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")  # Wypełnia mapę ścianami

        self.visible = np.full((width, height), fill_value=False, order="F")  # aktualnie widoczne
        self.explored = np.full((width, height), fill_value=False, order="F")  # widziane wcześniej
    def in_bounds(self, x: int, y: int) -> bool:
        """True, jeżeli x i y są w obszarze mapy"""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None :
        """
        Renderuje mape

        Jeżeli miejsce jest w tablicy 'visible' renderowana jest jako 'light'
        jeżeli jest w tablicy 'explored' renderowana jest jako 'dark'
        w innym wypadku (nie została jeszcze zobaczona) renderowana jako SHROUD
        """
        console.rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        )