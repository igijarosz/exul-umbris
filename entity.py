from typing import Tuple


class Entity:
    """
    Object representing players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char  # Visual representation of the entity
        self.color = color  # Color of the entity

    def move(self, dx: int, dy: int) -> None:
        #  Move entity by amount specified by dx and dy
        self.x += dx
        self.y += dy


