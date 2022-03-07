import pygame as pg
pg.init()

WIDTH, HEIGHT = 800, 600
is_running = True

pg.display.set_caption('')
pg.display.set_mode((WIDTH, HEIGHT))

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False