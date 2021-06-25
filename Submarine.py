import pygame
from Obst import Obstacle 

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

        self.exists      = True

        self.rect        = self.create_rect()

    def create_rect(self):
        return pygame.Rect(self.x, self.y,self.width, self.height)
                

    def move(self, window, velocity, acceleration, obstacles, spikes):
        keys = pygame.key.get_pressed()

        self.dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * velocity * acceleration
        self.dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * velocity * acceleration

        for obs in obstacles + spikes:
            if obs.rect.colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
                if isinstance(obs, Obstacle):
                    self.dx = 0
                    self.dy -= 1
                else:
                    self.exists = False

            if obs.rect.colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
                if isinstance(obs, Obstacle):
                    self.dy = 0
                else:
                    self.exists = False
        
        if not (0 <= self.x + self.dx <= 800 - self.width and 0 <= self.y + self.dy <= 800 - self.height):
            self.dy = 0
            self.dx = 0

        self.x += self.dx
        self.y += self.dy

        self.rect = self.create_rect()

    
    def flip(self, window):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.sign = 0
        if keys[pygame.K_LEFT]:
            self.sign = 1

