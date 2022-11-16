n = 6

SCREEN_WIDTH: int = 100 * n
SCREEN_HEIGHT: int = 100 * n



# TILE ATTRIBUTES

TILE_SIZE: int = SCREEN_WIDTH // n

INIT_STATE: list[list[int]] = [
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 0]
]

TILE_COLOR = (255, 255, 255)
