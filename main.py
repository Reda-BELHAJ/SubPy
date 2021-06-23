import pygame
import random

from pygame.display import update
from pygame.draw import rect
from Submarine import Submarine
from Bubble import Bubble

pygame.init()
pygame.display.set_caption('UNDERWATER')

# window  = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window  = pygame.display.set_mode((800, 800))
clock   = pygame.time.Clock()

bg      = pygame.image.load('Assets/bg.png')

submarine   = Submarine()

velocity        = 3
acceleration    = 0.9

bubbles = []

fog     = pygame.Surface((800, 800)).convert_alpha()

while True:
    clock.tick(60)

    window.blit(bg, (0 ,0))

    fog.fill((70, 70, 70))
    fog.set_alpha(100)

    window.blit(fog, (0 ,0), special_flags = pygame.BLEND_MULT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            quit()

    submarine.move(window, velocity, acceleration)
    submarine.flip(window)

    if submarine.sign == 0:
        window.blit(submarine.spriteR, (submarine.x,submarine.y))
    else:
        window.blit(submarine.spriteL, (submarine.x,submarine.y))

    
    if submarine.sign == 0:
        x, y = submarine.x + 10, submarine.y  - 5
    else:
        x, y = submarine.x + 30, submarine.y  - 8

    # bubble = Bubble(x ,y, 1)
    # bubbles.append(bubble)
    
    # window.blit(bubble.image, (bubble.x ,bubble.y))

    submarine.light(window)
    
    pygame.display.update()
    pygame.display.flip()