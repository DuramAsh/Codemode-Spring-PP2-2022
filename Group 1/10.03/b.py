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
speed = 1


running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                dx = speed
                dy = 0
            if event.key == pg.K_LEFT:
                dx = -speed
                dy = 0
            if event.key == pg.K_DOWN:
                dy = speed
                dx = 0
            if event.key == pg.K_UP:
                dy = -speed
                dx = 0
            if event.key == pg.K_SPACE:
                speed += 1
                if dx == 0:
                    dy = speed
                else:
                    dx = speed           
                # dx = speed 
                # dy = speed
        
    screen.fill(WHITE)
    pg.draw.ellipse(screen, color, (x % WIDTH, y % HEIGHT, 50, 50))
    print(speed, dx, dy)
    x += dx
    y += dy

    pg.display.flip()
pg.quit()
