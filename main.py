
import pygame
from Submarine import Submarine
from Light import *
from Maps.maps import map_list
import Map

pygame.init()
pygame.display.set_caption('UNDERWATER')

# window  = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window  = pygame.display.set_mode((800, 800))
clock   = pygame.time.Clock()

bg      = pygame.image.load('Assets/bg.png')

submarine   = Submarine(window)
light       = Light(submarine)

velocity        = 5
acceleration    = 0.9

fog     = pygame.Surface((800, 800)).convert_alpha()

map = map_list[0]

while True:
    clock.tick(60)

    window.blit(bg, (0 ,0))

    obstacles, spikes = Map.draw(map, window)

    fog.fill((70, 70, 70))

    window.blit(fog, (0 ,0), special_flags = pygame.BLEND_RGBA_MULT)

    if submarine.exists:
        submarine.move(window, velocity, acceleration, obstacles, spikes)
        submarine.flip(window)

        if submarine.sign == 0:
            window.blit(submarine.spriteR, (submarine.x,submarine.y))
        else:
            window.blit(submarine.spriteL, (submarine.x,submarine.y))

        light.create(window, submarine)

    pygame.display.update()
    pygame.display.flip()

    # Walls ??????
    # Bubble ?????
    # Animation destroy and fill the entire screen and goes to home screen
    # Zoom Camera : https://www.youtube.com/watch?v=0fS5LaXiQ-Q&ab_channel=RikCross
    # Switch Mode to 'radio scanning' and filter out the sprite hide
    # UI and cards to keep track of the health fuel mode charging 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  
            quit()