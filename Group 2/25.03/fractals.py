import pygame as pg
import math

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Fractal tree")
clock = pg.time.Clock()

running = True

theta = 90
r = 0.67


def branch(x1, y1, length, angle):
    if length <= 1:
        return
    x2 = x1 - length * math.cos(math.radians(angle))
    y2 = y1 - length * math.sin(math.radians(angle))
    if length <= 5:
        pg.draw.line(screen, GREEN, (x1, y1), (x2, y2), 2)
    else:
        pg.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)
    branch(x2, y2, length * r, angle + theta)
    branch(x2, y2, length * r, angle - theta)


while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(WHITE)
    # pg.draw.line(screen, BLACK, (WIDTH // 2, HEIGHT),
    #              (WIDTH // 2, HEIGHT - 100))

    x, y = pg.mouse.get_pos()
    r = (y / HEIGHT) * 0.7
    # theta = (x / WIDTH) * 180
    theta += 1
    if theta >= 360:
        theta = 0
    branch(WIDTH // 2, HEIGHT, 150, 90)

    pg.display.flip()
pg.quit()
