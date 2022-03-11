# moving circle
import pygame as pg
import random

pg.init()
pg.display.set_caption("Circle moving")
WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


color = GREEN
x = 350
y = 150
dx = 0
dy = 0


running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                x += 5
            if event.key == pg.K_LEFT:
                x -= 5
            if event.key == pg.K_DOWN:
                y += 5
            if event.key == pg.K_UP:
                y -= 5
            
            
        
    pg.draw.ellipse(screen, color, (x % WIDTH, y % HEIGHT, 50, 50))


    pg.display.flip()
pg.quit()
