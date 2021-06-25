from Walls import Walls
import pygame
import random

from pygame.display import update
from pygame.draw import rect
from Submarine import Submarine
from Bubble import Bubble
from Obst import Obstacle
from Light import *
import Map

pygame.init()
pygame.display.set_caption('UNDERWATER')

# window  = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window  = pygame.display.set_mode((800, 800))
clock   = pygame.time.Clock()

bg      = pygame.image.load('Assets/bg.png')

submarine   = Submarine(window)
light       = Light(submarine)

velocity        = 4
acceleration    = 0.9

fog     = pygame.Surface((800, 800)).convert_alpha()

obstacles = []


for x in range(3):
    obs     = Obstacle(300 * x, 50 * x)
    obstacles.append(obs)

while True:
    clock.tick(60)

    window.blit(bg, (0 ,0))
    obstacles = Map.draw(window)

    fog.fill((70, 70, 70))
    fog.set_alpha(100)

    window.blit(fog, (0 ,0), special_flags = pygame.BLEND_MULT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            quit()

    submarine.move(window, velocity, acceleration, obstacles)
    submarine.flip(window)

    if submarine.sign == 0:
        window.blit(submarine.spriteR, (submarine.x,submarine.y))
    else:
        window.blit(submarine.spriteL, (submarine.x,submarine.y))

    # if submarine.sign == 0:
    #     x, y = submarine.x + 10, submarine.y  - 5
    # else:
    #     x, y = submarine.x + 30, submarine.y  - 8

    # for obs in obstacles:
    #     window.blit(obs.sprite, (obs.x,obs.y))

    # for wall in walls:
    #     window.blit(wall.sprite, (wall.x,wall.y))

    light.create(window, submarine)

    pygame.display.update()
    pygame.display.flip()