INIT_STATE: list[list[int]] = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]
]


MAP_SIZE: int = len(INIT_STATE)

SCREEN_WIDTH: int = 100 * MAP_SIZE
SCREEN_HEIGHT: int = 100 * MAP_SIZE



# TILE ATTRIBUTES

TILE_SIZE: int = SCREEN_WIDTH // MAP_SIZE
TILE_ALIVE_COLOR: tuple[int, int, int] = (255, 255, 255)
TILE_DEAD_COLOR: tuple[int, int, int] = (0, 0, 0)
