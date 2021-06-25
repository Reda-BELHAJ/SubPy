import pygame

class Walls:
    def __init__(self, x, y):
        self.sprite = pygame.image.load('Assets/ceiling.png')
        self.width, self.height = self.sprite.get_size()
        self.x = x
        self.y = y

        self.rect = self.create_rect()

    def create_rect(self):
        return pygame.Rect(self.x, self.y,self.width, self.height)