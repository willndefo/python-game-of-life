import pygame
from utils.enums import Stage
from utils.constants import WHITE
from game_of_life.menu import Menu
from game_of_life.grid import Grid
from game_controller.button import Button


class GameOfLife:
    def __init__(self, width: int, height: int, tile_size: int):
        self.grid = Grid(width, height, tile_size)

        # Initialize pygame
        pygame.init()
        default_size = (width * tile_size, height * tile_size)
        self.screen: pygame.surface.Surface = pygame.display.set_mode(default_size, pygame.RESIZABLE)
        self.screen.fill(WHITE)
        self.clock = pygame.time.Clock()

        # Define the intro menu
        self.menu = Menu([
            Button("RANDOM"),
            Button("CUSTOM"),
            Button("SETTINGS")
        ])

        # Initialize stage
        self.stage = Stage.INTRO

    def play(self) -> None:
        """
            Launch the game
            :return: None
        """
        done: bool = False

        # While the game is not over
        while not done:

            if self.stage == Stage.INTRO:
                self.__intro_stage()
            elif self.stage == Stage.RANDOM:
                self.__random_stage()
            elif self.stage == Stage.CUSTOM:
                self.__custom_stage()
            elif self.stage == Stage.SETTINGS:
                self.__settings_stage()

            # Listen for all events
            for event in pygame.event.get():
                self.menu.handle_mouse_event()

                # Resize the screen game if the user resize the window
                if event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.screen.fill(WHITE)

                # Quit the infinite loop when the user presses the close button
                if event.type == pygame.QUIT:
                    done = True

            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()

    def __intro_stage(self) -> None:
        w = 200
        h = 50
        x0 = (self.screen.get_width() - w) // 2
        y0 = (self.screen.get_height() - h) // 2

        self.menu.update_button_rect(x0, y0, w, h)
        self.menu.draw(self.screen)

        # Update stage
        self.stage = self.menu.current_stage

    def set_stage(self, stage):
        self.stage = stage

    def __random_stage(self) -> None:
        self.grid.update_state()
        self.grid.draw_state(self.screen)

    def __custom_stage(self) -> None:
        print("CUSTOM STAGE")

    def __settings_stage(self) -> None:
        print("SETTINGS STAGE")
