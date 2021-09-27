import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (200, 200, 200), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100, 0)
polygon(screen, (0, 0, 0), [(100, 100), (190, 165), (180, 175), (90, 110), 
                            (100, 100)], 0)
polygon(screen, (0, 0, 0), [(300, 100), (210, 165), (220, 175), (310, 110), 
                            (300, 100)], 0)
circle(screen, (255, 0, 0), (150, 190), 30, 0)
circle(screen, (0, 0, 0), (150, 190), 10, 0)
circle(screen, (255, 0, 0), (250, 190), 30, 0)
circle(screen, (0, 0, 0), (250, 190), 10, 0)
rect(screen, (0, 0, 0), (150, 250, 100, 30))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()