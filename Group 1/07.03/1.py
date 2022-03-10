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

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('MY FIRST GAME')
clock = pg.time.Clock()
x = 0
y = 100
dx = 2
dy = 2

while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    screen.fill(WHITE)
    
    
    pg.draw.rect(screen, BLACK, (x, y, 100, 100)) # (экран, цвет, (х0, у0, ширина, высота), ширина рамки)
    # pg.draw.rect(screen, RED, (WIDTH // 2 - 30, HEIGHT // 2 - 30, 60, 60))
    x += dx
    y += dy
    if x == WIDTH-100 or x == 0:
        dx *= (-1)
    if y == HEIGHT-100 or y == 0:
        dy *= (-1)
    
    
    
    # for i in range(0, 100, 10):
    #     pg.draw.line(screen, BLUE, (0, 15+i), (100, 15+i), 1)
    
    # pg.draw.line(screen, BLUE, (100, 15), (300, 15), 3)
    
    
    pg.display.flip()
pg.quit()