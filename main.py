import pygame
from Submarine import Submarine

pygame.init()
pygame.display.set_caption('UNDERWATER')

# window  = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
window  = pygame.display.set_mode((800, 800))
clock   = pygame.time.Clock()

rect        = pygame.Rect(0, 0, 50, 50)
rect.center = window.get_rect().center

submarine   = Submarine()

velocity        = 2.4
acceleration    = 0.9

while True:
    clock.tick(60)
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

    submarine.light(window)
    
    pygame.display.update()
    pygame.display.flip()