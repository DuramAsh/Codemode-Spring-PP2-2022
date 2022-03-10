# moving circle
from uuid import RFC_4122
import pygame as pg
import random
import math

pg.init()
pg.display.set_caption("Circle moving")
WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

font = pg.font.SysFont("Georgia", 18)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

x, y = WIDTH // 2 + 250, HEIGHT // 2
angle = 0

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    screen.fill(WHITE)
    
    pg.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), 250, 5)
    pg.draw.circle(screen, GREEN, (x, y), 15)
    x = WIDTH // 2 + math.cos(math.radians(angle)) * 250
    y = HEIGHT // 2 - math.sin(math.radians(angle)) * 250
    angle += 1

    text1 = f'sin({angle % 360}) = {math.sin(math.radians(angle)):.2f}'
    text2 = f'cos({angle % 360}) = {math.cos(math.radians(angle)):.2f}'

    r1 = font.render(text1, True, RED)
    r2 = font.render(text2, True, BLUE)

    screen.blit(r1, (10, 0))
    screen.blit(r2, (10, 25))

    pg.display.flip()
pg.quit()
