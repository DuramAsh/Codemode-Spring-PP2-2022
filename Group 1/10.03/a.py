# space button
# квадрат бьется об стенку, отражается, и меняет цвет при нажатии на пробел
from unittest import runner
import pygame as pg
import random

pg.init()
pg.display.set_caption("Square moving")
WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

rect_x, rect_y = 70, 70
dx, dy = 3, 3
x = 300
y = 150

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(WHITE)

    pg.draw.rect(screen, RED, (x, y, rect_x, rect_y))
    x += dx
    y += dy

    if x >= WIDTH - rect_x or x <= 0:
        dx *= -1
    
    if y >= HEIGHT - rect_y or y <= 0:
        dy *= -1

    pg.display.flip()
pg.quit()
