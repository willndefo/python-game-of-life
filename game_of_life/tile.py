from utils.constants import TILE_ALIVE_COLOR, TILE_DEAD_COLOR
from pygame.surface import Surface as pySurface
from pygame.draw import rect as draw_rect


class Tile:
    def __init__(self, x: int, y: int, size: int, state: int):
        self.x: int = x
        self.y: int = y
        self.size: int = size
        self.state: int = state

    def draw(self, screen: pySurface) -> None:
        """
            Draw a tile
            :param screen: window where the game is displayed
            :return: nothing
        """
        color: tuple[int, int, int] = TILE_ALIVE_COLOR if self.state == 1 else TILE_DEAD_COLOR
        draw_rect(screen, color, (self.x * self.size, self.y * self.size, self.size, self.size))

    def set_state(self, state):
        self.state = state
