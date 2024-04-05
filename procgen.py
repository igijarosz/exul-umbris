import random
from typing import Iterator, Tuple
from __future__ import annotations

import tcod
import tile_types
from game_map import GameMap


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property  # Pozwala na odwoływanie się do metody klasy jak do wartości klasy
    def center(self) -> Tuple[int, int]:
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        """Zwraca wnętrze pokoju jako index tablicy 2D"""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)


    def intersects(self, other: RectangularRoom) -> bool:
        """Zwraca True, jeżeli pokoje się nakładają"""
        return (
            self.x1 <= other.x2
            and self.x2 >= other.x1
            and self.y1 <= other.y2
            and self.y2 >= other.y1
        )


def tunnel_between(start: Tuple[int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    """Zwraca tunel w kształcie L pomiędzy dwoma punktami"""
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:
        # najpierw poziomo potem pionowo
        corner_x, corner_y = x2, y1
    else:
        # najpierw pionowo potem poziomo
        corner_x, corner_y = x1, y2

    for x, y in list(tcod.los.bresenham((x1, y1), (corner_x, corner_y))):
        yield x, y
    for x, y in list(tcod.los.bresenham((corner_x, corner_y), (x2, y2))):
        yield x, y


def generate_dungeon(map_width, map_height) -> GameMap:
    dungeon = GameMap(map_width, map_height)

    room_1 = RectangularRoom(x=20, y=25, width=10, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)

    dungeon.tiles[room_1.inner] = tile_types.floor
    dungeon.tiles[room_2.inner] = tile_types.floor

    for x, y in tunnel_between(room_2.center, room_1.center):
        dungeon.tiles[x, y] = tile_types.floor

    return dungeon