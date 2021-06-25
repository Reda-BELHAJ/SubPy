import pygame
from Obst import Obstacle

map = """
WWWWWWWWWWWWWWWWW
W               W
W               W
W               W
W               W
W         O     W
W               W
W               W
W               W
W               W
W      OOOO     W
W               W
W       O       W
W               W
W               W
W               W
WWWWWWWWWWWWWWWWW
"""

map = map.splitlines()

def draw(window):
    obstacles = []
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c == "O":
                tile = Obstacle(x * 48, y * 48)
                obstacles.append(tile)
                window.blit(tile.sprite, (tile.x, tile.y))
    
    return obstacles