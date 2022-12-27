"""
    Description: Implementation of game of life, a Jon Conway's algorithm
    Author: Wilfried Ndefo
    Inspiration: https://www.youtube.com/watch?v=S-W0NX97DB0
"""

from game_of_life.game import GameOfLife
from utils.constants import MAP_WIDTH, MAP_HEIGHT, TILE_SIZE

if __name__ == "__main__":
    gol = GameOfLife(MAP_WIDTH, MAP_HEIGHT, TILE_SIZE)
    gol.play()
