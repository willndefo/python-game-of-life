import pygame
from utils.parameter import Parameter


class TextField:
    def __init__(self, screen: pygame.surface.Surface, label: str, pos_x: int, pos_y: int, default_input: str = ""):
        self.input: str = default_input  # Content of the textfield
        self.label: str = label  # Label of the textfield

        # Initialize the textfield rect
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y
        self.width: int = 200
        self.height: int = 30
        self.rect_boundary = pygame.Rect(pos_x, pos_y, self.width, self.height)

        # Define stroke rectangle
        self.stroke = 3  # Outline width

        self.screen: pygame.surface.Surface = screen
        self.font = pygame.font.Font(None, Parameter.font_size)
        self.active: bool = False

    def draw(self) -> None:
        # Draw the rectangle field
        pygame.draw.rect(self.screen, Parameter.bg_color, self.rect_boundary)

        # Draw line stroke at the bottom
        start = (self.pos_x, self.pos_y + self.height)
        end = (self.pos_x + self.width, self.pos_y + self.height)
        color = Parameter.grid_color if self.active else Parameter.font_color
        pygame.draw.line(self.screen, color, start, end, self.stroke)

        # Render the text and draw it to the screen
        text_surface = self.font.render(self.input, True, Parameter.font_color)
        text_rect = text_surface.get_rect(midleft=self.rect_boundary.midleft)
        self.screen.blit(text_surface, text_rect)

        # Render text label
        text_surface = self.font.render(self.label, True, Parameter.font_color)
        text_rect = text_surface.get_rect(centery=self.rect_boundary.centery)
        self.screen.blit(text_surface, text_rect)

    def handle_typing(self, event: pygame.event.Event) -> None:

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect_boundary.collidepoint(event.pos):  # Check if the mouse click on the field
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                else:
                    self.input += event.unicode
