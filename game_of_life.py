import pygame
from constants import *
import numpy as np

class Game_Of_Life:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.tile_size = TILE_SIZE

        # Initialize the init grid
        self.state = INIT_STATE

        # Initialize pygame
        pygame.init()

        self.screen: pygame.surface.Surface = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        def play():
            done: bool = False

            # While the game is not over
            while not done:

                # state = get_next_state(state)
                #
                # for row in range(1, len(state) - 1):
                #     for col in range(1, len(state) - 1):
                #         if state[row][col] == 1:
                #             draw_at_case(row, col, TILE_ALIVE_COLOR)
                #         else:
                #             draw_at_case(row, col, TILE_DEAD_COLOR)


                # Listen for all events
                for event in pygame.event.get():

                    # Quit the infinite loop when the user presses the close button
                    if event.type == pygame.QUIT:
                        done = True

                self.clock.tick(1)

            pygame.quit()
