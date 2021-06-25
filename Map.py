import pygame
from Obst import Obstacle
from Spike import Spike

map = """
WWWWWWWWWWWWWWWWW
W               W
W               W
W               W
W               W
W         S     W
W               W
W               W
W               W
W               W
W      OOOOOOOOOO
W        S      W
W        S      W
W               W
W     OOOOOOOOOOO
W               W
WWWWWWWWWWWWWWWWW
"""

map = map.splitlines()

def draw(window):
    spikes = []
    obstacles = []
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c == "O":
                obs = Obstacle(x * 48, y * 48)
                obstacles.append(obs)
                window.blit(obs.sprite, (obs.x, obs.y))
            
            if c == "S":
                spike = Spike(x * 48, y * 48)
                spikes.append(spike)
                window.blit(spike.sprite, (spike.x, spike.y))
    
    return obstacles, spikes