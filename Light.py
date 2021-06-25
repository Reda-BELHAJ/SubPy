import pygame 

class Light:
    def __init__(self, submarine):
        self.spritR = pygame.image.load('Assets/lightTT.png').convert_alpha()
        self.spritL = pygame.transform.flip(self.spritR, True, False)

        self.x ,self.y = self.update(submarine)
    
    def update(self, submarine):
        self.x           = submarine.x + 24.5 + submarine.width/2
        self.y           = submarine.y + 7 + submarine.height/2

        if submarine.sign == 1:
            self.x  -= submarine.width - 4

        return self.x, self.y

    def create(self, window, submarine):
        self.update(submarine)

        lightRect  = self.spritR.get_rect()
        lightRect.center = (self.x, self.y)

        self.spritR.set_alpha(120)
        self.spritL.set_alpha(120)

        if submarine.sign == 0:
            window.blit(self.spritR, lightRect)
        else:
            window.blit(self.spritL, lightRect)