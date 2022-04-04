import pygame as pg

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Surface")
clock = pg.time.Clock()

running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # if event.type == pg.MOUSEBUTTONDOWN:
        #     keys = pg.mouse.get_pressed()
        #     if keys[0]:
        #         print("LMB")
        #     elif keys[1]:
        #         print("KOLESIKO")
        #     else:
        #         print("RMB")

    if pg.mouse.get_pressed()[0]:
        print("PRESS")

    screen.fill(WHITE)

    pg.display.flip()
pg.quit()
