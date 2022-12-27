from utils.enums import Stage
from game_controller.button import Button
from pygame.surface import Surface as pySurface


class Menu:
    def __init__(self, buttons: list[Button]):
        self.buttons = buttons
        self.current_stage = Stage.INTRO

    def handle_mouse_event(self) -> None:
        for button in self.buttons:
            button.handle_mouse_event()

            if button.is_clicked:
                self.current_stage = Stage[button.label]

    def draw(self, screen: pySurface) -> None:
        for button in self.buttons:
            button.draw(screen)

    def update_button_rect(self, x: int, y: int, w: int, h: int) -> None:
        """
            Update button boundaries in case of window resizing
            :param x: x coordinate of the top left border of the button
            :param y: y coordinate of the top left border of the button
            :param w: width of the button
            :param h: height of the button
            :return: nothing
        """
        offset = -h * 2
        for button in self.buttons:
            button.set_button_rect(x, y + offset, w, h)
            offset += h * 2
