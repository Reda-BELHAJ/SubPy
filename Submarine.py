import pygame
import pygame.gfxdraw as gfx

class Submarine:
    def __init__(self) :
        self.spriteR     = pygame.image.load('Assets/SubMarine.png')
        self.spriteL     = pygame.transform.flip(self.spriteR, True, False)
        self.x           = 100
        self.y           = 100
        self.sign        = 0

    def light(self, window):
        xPlus, yPlus = self.spriteR.get_size()
        lightR       = pygame.image.load('Assets/lightTT.png').convert_alpha()

        xL           = self.x + 24.5 + xPlus/2
        yL           = self.y +7+ yPlus/2

        if self.sign == 1:
            lightR   = pygame.transform.flip(lightR, True, False)
            xL -= xPlus - 4

        lightR.set_alpha(100)

        lightRect  = lightR.get_rect()
        lightRect.center = (xL, yL)

        window.blit(lightR, lightRect)
                

    def move(self, window, velocity, acceleration):
        keys = pygame.key.get_pressed()
    
        self.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * velocity * acceleration
        self.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * velocity * acceleration

        window.fill((20, 20, 50))

    
    def flip(self, window):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.sign = 0
        if keys[pygame.K_LEFT]:
            self.sign = 1

