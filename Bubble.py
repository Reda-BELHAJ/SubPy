import pygame
import random

IMAGE = ['Bubble.png', 'bubbles.png', 'Bubble.png']

class Bubble:
    def __init__(self,x , y, i):
        self.image  = pygame.image.load('Assets/' + IMAGE[i])
        self.x      = x
        self.y      = y

        self.velocity = 0
        self.accel    = 0
        self.exists   = True
    
    def update(self, y):
        self.y -= 1
        # self.x += random.randint(-1,1)

        if self.y < y - 20 or self.y > y + 20:
            self.exists   = False