import pygame


class Button:
    def __init__(self, x: int, y: int, w: int, h, text: str, font_size: int):
        # Set the button dimensions and position
        self.rect = pygame.Rect(x, y, w, h)

        # Initialize the font and render the text
        self.font = pygame.font.Font(None, font_size)
        self.text = self.font.render(text, True, (255, 255, 255))

        # Initialize the color
        self.color = (0, 0, 0)

    def draw(self, screen) -> None:
        """
            Draw the button
            :param screen: window where the game is displayed
            :return: nothing
        """

        # Draw the button rectangle
        pygame.draw.rect(screen, self.color, self.rect)

        # Draw text label
        text_rect = self.text.get_rect(center=self.rect.center)
        screen.blit(self.text, text_rect)

    def handle_click(self, event) -> None:
        """
            Responsible to trigger an action when the user click on the button
            :param event: event catch from the pygame area
            :return: nothing
        """

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("Hello World")
