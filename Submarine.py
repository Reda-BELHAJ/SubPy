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

        if self.sign == 0:
            xPlus += self.x
            xP     = xPlus + 160
            xB     = xP - 40
        else:
            xPlus += self.x - xPlus
            xP     = xPlus - 160
            xB     = xP + 40
        
        yPlus += self.y - 10

        surf1     = pygame.Surface((800, 800), pygame.SRCALPHA)
        surf2     = pygame.Surface((800, 800), pygame.SRCALPHA)
        
        pygame.draw.polygon(surf1,(255, 255, 255),[(xPlus,yPlus),(xP,yPlus + 80), (xP,yPlus - 80)])

        # yB1 = 0.5 * xB + 47.5
        # yB2 = - 0.5 * xB + 200.5

        pygame.draw.polygon(surf2,(255, 255, 255),[(xPlus,yPlus),(xB,yPlus + 60), (xB,yPlus - 60)])

        surf1.set_alpha(20)
        window.blit(surf1, (0,0))

        surf2.set_alpha(5)
        window.blit(surf2, (0,0))
                

    def move(self, window, velocity, acceleration):
        keys = pygame.key.get_pressed()
    
        self.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * velocity * acceleration
        self.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * velocity * acceleration

        window.fill((11, 4, 54))

    
    def flip(self, window):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.sign = 0
        if keys[pygame.K_LEFT]:
            self.sign = 1

