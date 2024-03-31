import tcod.event
from typing import Optional

from actions import Action, MovementAction, EscapeAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:  # Receiving keypresses
        action: Optional[Action] = None

        key = event.sym

        match key:
            case tcod.event.KeySym.UP:
                action = MovementAction(dx=0, dy=-1)
            case tcod.event.KeySym.DOWN:
                action = MovementAction(dx=0, dy=1)
            case tcod.event.KeySym.LEFT:
                action = MovementAction(dx=-1, dy=0)
            case tcod.event.KeySym.RIGHT:
                action = MovementAction(dx=1, dy=0)

            case tcod.event.KeySym.ESCAPE:
                action = EscapeAction()

        return action
