import pygame

class Submarine:
    def __init__(self) :
        self.spriteR     = pygame.image.load('Assets/SubMarine.png')
        self.spriteL     = pygame.transform.flip(self.spriteR, True, False)
        self.x           = 0
        self.y           = 0
        self.sign        = 0


    def light(self, window):
        xPlus, yplus = self.spriteR.get_size()
        xP, yP       = 0, 0
        if self.sign == 0:
            xPlus += self.x
            xP     = xPlus + 160
        else:
            xPlus += self.x - xPlus
            xP     = xPlus - 160
        
        yplus += self.y - 10

        pygame.draw.polygon(
            window,
            (255, 255, 255, 0),
            [
            (xPlus,yplus),(xP,yplus + 80), (xP,yplus - 80)
            ])
                

    def move(self, window, velocity, acceleration):
        keys = pygame.key.get_pressed()
    
        self.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * velocity * acceleration
        self.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * velocity * acceleration

        self.x = self.x % window.get_width()
        self.y = self.y % window.get_height()

        window.fill((11, 4, 54))

    
    def flip(self, window):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.sign = 0
        if keys[pygame.K_LEFT]:
            self.sign = 1

