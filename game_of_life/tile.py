import pygame
from utils.type import Color
from pygame.draw import rect as draw_rect
from utils.parameter import Parameter
from pygame.surface import Surface as pySurface


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

        color: Color = Parameter.tile_alive_color if self.state == 1 else Parameter.tile_dead_color
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
