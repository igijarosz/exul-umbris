from typing import Tuple


class Entity:
    """
    Klasa reprezentująca wszysstkie jednostki. Graczy, npc, przeciwników itp.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char  # Znak używany do reprezentacji postaci
        self.color = color  # Kolor postaci

    def move(self, dx: int, dy: int) -> None:
        #  przesuń jednostkę o dx i dy
        self.x += dx
        self.y += dy


