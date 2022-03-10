import pygame as pg
pg.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
is_running = True

fps = 60
x, y = 100, 100
dx = 5
dy = 0

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('MY FIRST GAME')
clock = pg.time.Clock()

while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    screen.fill(WHITE)
    
    pg.draw.rect(screen, BLACK, (100, 100, 600, 400), 1)
    pg.draw.circle(screen, RED, (x, y), 15)
    x += dx
    y += dy
    if x == 700 and y == 100:
        dx = 0
        dy = 5
    elif x == 700 and y == 500:
        dy = 0
        dx = -5
    elif x == 100 and y == 500:
        dx = 0
        dy = -5
    elif x == 100 and y == 100:
        dx = 5
        dy = 0

    pg.display.flip()
pg.quit()
