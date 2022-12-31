import pygame
from utils.type import Color
from pygame.draw import rect as draw_rect
from pygame.surface import Surface as pySurface
from utils.constants import TILE_ALIVE_COLOR, TILE_DEAD_COLOR


class Tile:
    def __init__(self, x: int, y: int, size: int, state: int):
        self.state: int = state
        self.rect = pygame.Rect(x * size, y * size, size, size)
        self.click_flag: int = 0  # Control variable for handle click because of the game's loop

    def draw(self, screen: pySurface) -> None:
        """
            Draw a tile
            :param screen: window where the game is displayed
            :return: nothing
        """

        color: Color = TILE_ALIVE_COLOR if self.state == 1 else TILE_DEAD_COLOR
        draw_rect(screen, color, self.rect)

    def toggle_state(self) -> None:
        """
            Responsible to switch between the state value of state (0, 1) by click
            :return: nothing
        """

        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and self.click_flag < 1:
                self.set_state(int(not self.state))
                self.click_flag += 1
        else:
            self.click_flag = 0

    def set_state(self, state: int):
        self.state = state
