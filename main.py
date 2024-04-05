import tcod
from entity import Entity
from engine import Engine
from procgen import generate_dungeon
from input_handlers import EventHandler


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 5
    max_rooms = 20

    tileset = tcod.tileset.load_tilesheet(
        "font.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2), int(screen_height / 2), "N", (255, 255, 0))
    entities = {npc, player}

    game_map = generate_dungeon(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(  # Utworzenie terminalu/ekranu
            screen_width,
            screen_height,
            tileset=tileset,
            title="Exul Umbris",
            vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:  # Game loop
            engine.render(console=root_console, context=context)  # Renderowanie

            events = tcod.event.wait()  # Oczekiwanie na input

            engine.handle_events(events)  # Wysłanie eventu do metody danego eventu


if __name__ == "__main__":
    main()
