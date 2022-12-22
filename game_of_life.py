"""
    Description: Implementation of the class game of life, a Jon Conway's algorithm
    Author: Wilfried Ndefo
    Inspiration: https://www.youtube.com/watch?v=S-W0NX97DB0
"""
import pygame
from constants import *


class GameOfLife:
    def __init__(self):
        self.width: int = MAP_WIDTH
        self.height: int = MAP_HEIGHT
        self.tile_size: int = TILE_SIZE

        # Initialize the init grid
        self.state: list[list[int]] = INIT_STATE

        # Initialize pygame
        pygame.init()
        self.screen: pygame.surface.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def play(self) -> None:
        """
            Launch the game
            :return: None
        """
        done: bool = False

        # While the game is not over
        while not done:

            self.update_state()

            self.draw_state()

            # Listen for all events
            for event in pygame.event.get():

                # Quit the infinite loop when the user presses the close button
                if event.type == pygame.QUIT:
                    done = True

            pygame.display.flip()
            self.clock.tick(1)

        pygame.quit()

    def draw_state(self) -> None:
        """
            Responsible to draw the current state
            :return:
        """
        self.screen.fill((0, 0, 0))

        for x in range(0, self.width):
            for y in range(0, self.height):
                color = TILE_ALIVE_COLOR if self.state[y][x] == 1 else TILE_DEAD_COLOR
                pygame.draw.rect(self.screen, color,
                                 (x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size))

    def update_state(self) -> None:
        """
            Responsible to apply rules of the gol and update the state
            :return: nothing
        """

        # At init next_state is a zero matrix
        next_state: list[list[int]] = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for x in range(self.width):
            for y in range(self.height):

                # Check rules
                if 2 <= self.get_neighbours_number(x, y) <= 3:  # 2 <= n < 3 and n == 3 stay alive
                    next_state[y][x] = 1
                elif 3 < self.get_neighbours_number(x, y):
                    next_state[y][x] = 0

        # Pass the current state to the next
        self.state = next_state

    def get_neighbours_number(self, x: int, y: int) -> int:
        """
            Check the number of neighbours
            :param x: position x of the tile in the map
            :param y: position y of the tile in the map
            :return: neighbours number
        """
        number: int = 0

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                    number += 1 if self.state[y + dy][x + dx] == 1 else 0

        return number


if __name__ == "__main__":
    gol = GameOfLife()
    gol.play()
