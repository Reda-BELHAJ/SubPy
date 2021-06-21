import pygame

img = pygame.image.load('Assets/light_350_med.png')
img.set_colorkey((255, 0, 255))

c = (img.get_width()/2, img.get_height()/2)
ne = (img.get_width(), 0)
nw = (0, 0)
sw = (0, img.get_height())
se = (img.get_width(), img.get_height())

points = (c, ne, nw, sw, se)

pygame.draw.polygon(img, (255, 0, 255), points, 0)

finsurf = pygame.Surface(img.get_size(), pygame.SRCALPHA)

finsurf.blit(img, (0, 0))

pygame.image.save(finsurf, "lightT.png")