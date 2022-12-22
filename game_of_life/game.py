import pygame
from game_of_life.grid import Grid


class GameOfLife:
    def __init__(self, width: int, height: int, tile_size: int):
        self.grid = Grid(width, height, tile_size)

        # Initialize pygame
        pygame.init()
        self.screen: pygame.surface.Surface = pygame.display.set_mode((width * tile_size, height * tile_size))
        self.clock = pygame.time.Clock()

    def play(self) -> None:
        """
            Launch the game
            :return: None
        """
        done: bool = False

        # While the game is not over
        while not done:

            self.grid.update_state()

            self.grid.draw_state(self.screen)

            # Listen for all events
            for event in pygame.event.get():

                # Quit the infinite loop when the user presses the close button
                if event.type == pygame.QUIT:
                    done = True

            pygame.display.flip()
            self.clock.tick(1)

        pygame.quit()
