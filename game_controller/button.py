import pygame
from utils.type import Color
from utils.constants import BLACK, WHITE


class Button:
    def __init__(self, label: str = "Button", font_size: int = 24):
        # Set the button dimensions and position
        self.rect = pygame.Rect(0, 0, 0, 0)

        # Initialize the font and render the text
        self.font = pygame.font.Font(None, font_size)
        self.text_color: Color = WHITE
        self.label: str = label
        self.text = self.font.render(label, True, self.text_color)

        # Initialize the color
        self.bg_color: Color = BLACK

        # Initialize the action
        self.is_clicked: bool = False

    def draw(self, screen) -> None:
        """
            Draw the button
            :param screen: window where the game is displayed
            :return: nothing
        """

        # Draw the button rectangle
        pygame.draw.rect(screen, self.bg_color, self.rect)

        # Draw text label
        self.text = self.font.render(self.label, True, self.text_color)
        text_rect = self.text.get_rect(center=self.rect.center)
        screen.blit(self.text, text_rect)

    def set_button_rect(self, x: int, y: int, w: int, h: int):
        self.rect = pygame.Rect(x, y, w, h)

    def handle_mouse_event(self) -> None:
        """
            Responsible to trigger an action when the user click on the button
            :return: nothing
        """

        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            self.bg_color, self.text_color = WHITE, BLACK  # Mouseover

            if pygame.mouse.get_pressed()[0] == 1 and not self.is_clicked:  # Mouseclick
                self.is_clicked = True
        else:  # Exit Mouseover
            self.bg_color, self.text_color = BLACK, WHITE

        if pygame.mouse.get_pressed()[0] == 0:  # Exit MouseClick
            self.is_clicked = False
