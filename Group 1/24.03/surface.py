from ast import While
import pygame as pg

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Surface")

surf = pg.Surface((400, 400))
# surf = pg.Surface((400, 400), pg.SRCALPHA) --прозрачный
surf.fill(RED)

surf2 = pg.Surface((400, 200))
surf2.fill((0, 255, 0))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = 0
    screen.fill(WHITE)
    pg.draw.circle(surf, BLACK, (100, 50), 25)

    surf.blit(surf2, (10, 200))
    screen.blit(surf, (100, 100))
    


    pg.display.update()
pg.quit()