import pygame
import pygame.draw as pgd
from math import sin, cos, pi

pygame.init()

FPS = 30
screen = pygame.display.set_mode((910, 600))


def sun(x, y, n, r1, r2):
    spt = []
    for i in range(n * 2):
        a = 2 * pi * i / (2 * n)
        if i % 2 == 0:
            xt = int(r1 * cos(a))
            yt = int(r1 * sin(a))
        else:
            xt = int(r2 * cos(a))
            yt = int(r2 * sin(a))
        xt += x
        yt += y
        spt.append((xt, yt))
    pgd.polygon(screen, (255, 100, 100), spt, 0)
    pgd.polygon(screen, (0, 0, 0), spt, 1)


def cloud(x, y, r):
    pgd.circle(screen, (255, 255, 255), (x + r, y + 2 * r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + r, y + 2 * r), r, 1)
    pgd.circle(screen, (255, 255, 255), (x + 2 * r, y + 2 * r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + 2 * r, y + 2 * r), r, 1)
    pgd.circle(screen, (255, 255, 255), (x + 3 * r, y + 2 * r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + 3 * r, y + 2 * r), r, 1)
    pgd.circle(screen, (255, 255, 255), (x + 4 * r, y + 2 * r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + 4 * r, y + 2 * r), r, 1)
    pgd.circle(screen, (255, 255, 255), (x + 3 * r, y + r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + 3 * r, y + r), r, 1)
    pgd.circle(screen, (255, 255, 255), (x + 2 * r, y + r), r, 0)
    pgd.circle(screen, (0, 0, 0), (x + 2 * r, y + r), r, 1)


def tree(x, y, s):
    k = 0.8
    pgd.rect(screen, (0, 0, 0), (x + s * 3 // 7, int(y + s * k), s // 7, s))
    pgd.circle(screen, (0, 255, 0), (x + s // 2, int(y + s * k // 4)), s // 4,
               0)
    pgd.circle(screen, (0, 0, 0), (x + s // 2, int(y + s * k // 4)), s // 4, 1)
    pgd.circle(screen, (0, 255, 0), (x + s // 4, int(y + s * k // 2)), s // 4,
               0)
    pgd.circle(screen, (0, 0, 0), (x + s // 4, int(y + s * k // 2)), s // 4, 1)
    pgd.circle(screen, (0, 255, 0), (x + s * 3 // 4, int(y + s * k // 2)),
               s // 4, 0)
    pgd.circle(screen, (0, 0, 0), (x + s * 3 // 4, int(y + s * k // 2)),
               s // 4, 1)
    pgd.circle(screen, (0, 255, 0), (x + s // 2, int(y + s * k * 3 // 4)),
               s // 4, 0)
    pgd.circle(screen, (0, 0, 0), (x + s // 2, int(y + s * k * 3 // 4)),
               s // 4, 1)
    pgd.circle(screen, (0, 255, 0), (x + s // 4, int(y + s * k)), s // 4, 0)
    pgd.circle(screen, (0, 0, 0), (x + s // 4, int(y + s * k)), s // 4, 1)
    pgd.circle(screen, (0, 255, 0), (x + s * 3 // 4, int(y + s * k)), s // 4,
               0)
    pgd.circle(screen, (0, 0, 0), (x + s * 3 // 4, int(y + s * k)), s // 4, 1)


def house(x, y, s):
    pgd.rect(screen, (204, 119, 34), (x, y + s, 2 * s, int(1.5 * s)))
    pgd.rect(screen, (0, 0, 0), (x, y + s, 2 * s, int(1.5 * s)), 1)
    pgd.rect(screen, (150, 150, 255), (x + s * 3 // 4, y + int(1.5 * s),
                                       s // 2, s // 2))
    pgd.rect(screen, (190, 100, 34), (x + s * 3 // 4, y + int(1.5 * s),
                                      s // 2, s // 2), 5)
    pgd.polygon(screen, (255, 100, 100), [(x, y + s), (x + s, y), (x + 2 * s,
                                                                   y + s)], 0)
    pgd.polygon(screen, (0, 0, 0), [(x, y + s), (x + s, y), (x + 2 * s,
                                                             y + s)], 1)
    kt = 13
    for i in range(kt + 1):
        pgd.polygon(screen, (100, 100, 100), [(x + s - i * int(s // kt),
                                               y + i * int(s // kt)),
                                              (x + s - (i + 1) * int(s // kt),
                                               y + (i + 1) * int(s // kt)),
                                              (x + s - i * int(s // kt),
                                               y + (i + 1) * int(s // kt))], 0)
    for i in range(kt + 1):
        pgd.polygon(screen, (100, 100, 100), [(x + s + i * int(s // kt),
                                               y + i * int(s // kt)),
                                              (x + s + (i + 1) * int(s // kt),
                                               y + (i + 1) * int(s // kt)),
                                              (x + s + i * int(s // kt),
                                               y + (i + 1) * int(s // kt))], 0)


pgd.rect(screen, (50, 50, 255), (0, 0, 910, 300))
pgd.rect(screen, (50, 255, 50), (0, 300, 910, 300))
sun(50, 50, 20, 40, 38)
cloud(150, 40, 35)
tree(320, 210, 140)
house(100, 230, 100)
house(500, 230, 80)
tree(700, 200, 110)
cloud(430, 100, 25)
cloud(700, 60, 37)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
