import pygame

class Submarine:
    def __init__(self, window) :
        self.spriteR     = pygame.image.load('Assets/SubMarine.png')
        self.spriteL     = pygame.transform.flip(self.spriteR, True, False)

        self.width, self.height = self.spriteR.get_size()

        self.x           = 100
        self.y           = 100
        self.sign        = 0

        self.dx          = 0
        self.dy          = 0

        self.rect        = self.create_rect(window)

    def create_rect(self, window):
        return pygame.Rect(self.x, self.y,self.width, self.height)

    def light(self, window):
        lightR       = pygame.image.load('Assets/lightTT.png').convert_alpha()
        # light_350_med

        xL           = self.x + 24.5 + self.width/2
        yL           = self.y + 7 + self.height/2

        if self.sign == 1:
            lightR   = pygame.transform.flip(lightR, True, False)
            xL -= self.width - 4

        lightR.set_alpha(100)

        lightRect  = lightR.get_rect()
        lightRect.center = (xL, yL)

        window.blit(lightR, lightRect)
                

    def move(self, window, velocity, acceleration, rects):
        keys = pygame.key.get_pressed()

        self.dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * velocity * acceleration
        self.dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * velocity * acceleration

        for rect in rects:
            if rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                self.dx = 0
                self.dy -= 1

            if rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                self.dy = 0
        
        if not (0 <= self.x + self.dx <= 800 - self.width and 0 <= self.y + self.dy <= 800 - self.height):
            self.dy = 0
            self.dx = 0

        self.x += self.dx
        self.y += self.dy

        self.rect = self.create_rect(window)

        # window.fill((20, 20, 50))

    
    def flip(self, window):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.sign = 0
        if keys[pygame.K_LEFT]:
            self.sign = 1

