# moving circle
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
GREEN = (0, 255, 0)

font = pg

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

    pg.display.flip()
pg.quit()
