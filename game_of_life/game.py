import pygame
from utils.enums import Stage
from utils.parameter import Parameter
from game_controller.stage_manager import StageManager


class GameOfLife:
    def __init__(self):
        # Load parameters from the settings file
        Parameter.load_from_file("settings.txt")

        # Initialize pygame
        pygame.init()
        self.screen: pygame.surface.Surface = pygame.display.set_mode(Parameter.default_size, pygame.RESIZABLE)
        self.screen.fill(Parameter.bg_color)
        self.clock = pygame.time.Clock()

        # Initialize stage manager
        self.stage_manager = StageManager(self.screen)

    def play(self) -> None:
        """
            Launch the game
            :return: None
        """
        done: bool = False

        # While the game is not over
        while not done:

            self.screen.fill(Parameter.bg_color)

            self.stage_manager.draw_stage(self.screen)
            self.stage_manager.update_stage()

            # Listen for all events
            for event in pygame.event.get():
                self.stage_manager.handle_event(event)

                # Resize the screen game if the user resize the window
                if event.type == pygame.VIDEORESIZE:
                    self.__resize_game(event)

                # Quit the infinite loop when the user presses the close button
                if event.type == pygame.QUIT:
                    Parameter.save_to_file("settings.txt")
                    done = True

            pygame.display.flip()
            if self.stage_manager.stage == Stage.PLAY:
                self.clock.tick(10)
            else:
                self.clock.tick(60)

        pygame.quit()

    def __resize_game(self, event: pygame.event.Event) -> None:
        # Force minimum dimension
        screen_width = max(Parameter.default_size.w, event.w)
        screen_height = max(Parameter.default_size.h, event.h)

        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
        self.screen.fill(Parameter.bg_color)
