import pygame as pg
from random import *

WIDTH = 800
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption("Hungry Lion")


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = 
        self.rect = self.surf.get_rect()


class Enemy(pg.sprite.Sprite):
    pass


class Coin(pg.sprite.Sprite):
    pass


running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()
pg.quit()
        
