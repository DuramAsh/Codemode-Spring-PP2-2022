import pygame as pg
pg.init()

WIDTH, HEIGHT = 800, 600
is_running = True

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('MY FIRST GAME')

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    
    screen.fill((255, 255, 255))
    pg.display.flip()
    
pg.quit()