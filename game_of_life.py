import pygame
from constants import *

pygame.init()

screen: pygame.surface.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()


def generate_map(_map: list):
    offset_y: int = 0
    for row in _map:
        offset_x: int = 0
        for col in row:
            if col == 1:
                pygame.draw.rect(screen, TILE_COLOR, (offset_x, offset_y, TILE_SIZE, TILE_SIZE))
            offset_x += TILE_SIZE

        offset_y += TILE_SIZE

    pygame.display.flip()


done: bool = False

# While the game is not over
while not done:

    generate_map(INIT_STATE)

    # Listen for all events
    for event in pygame.event.get():

        # Quit the infinite loop when the user presses the close button
        if event.type == pygame.QUIT:
            done = True

    clock.tick(1)

pygame.quit()
