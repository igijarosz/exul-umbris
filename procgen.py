from __future__ import annotations

import random
from typing import Iterator, Tuple, List, TYPE_CHECKING

import tcod
import tile_types
from game_map import GameMap

if TYPE_CHECKING:
    from entity import Entity


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


def generate_dungeon(
        max_rooms: int,
        room_min_size: int,
        room_max_size: int,
        map_width: int,
        map_height: int,
        player: Entity,
) -> GameMap:
    """Wygeneruj nową mapę"""
    dungeon = GameMap(map_width, map_height)

    rooms: List[RectangularRoom] = []

    for r in range(max_rooms):
        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        x = random.randint(0, dungeon.width - room_width - 1)
        y = random.randint(0, dungeon.height - room_height - 1)

        new_room = RectangularRoom(x, y, room_width, room_height)

        # przechodzi przez pokoje i sprawdza, czy nie nachodzą na siebie
        if any(new_room.intersects(other_room) for other_room in rooms):
            continue

        dungeon.tiles[new_room.inner] = tile_types.floor

        if len(rooms) == 0:
            # pokój, w którym zaczyna gracz
            player.x, player.y = new_room.center
        else:
            for x, y in tunnel_between(rooms[-1].center, new_room.center):
                dungeon.tiles[x, y] = tile_types.floor

        rooms.append(new_room)


    return dungeon
