import pygame as pg
pg.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
is_running = True

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('MY FIRST GAME')
clock = pg.time.Clock()


while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    
    screen.fill(WHITE)
    pg.draw.rect(screen, BLACK, (WIDTH // 2 - 50, HEIGHT // 2 - 50, 100, 100))

    pg.display.flip()
pg.quit()