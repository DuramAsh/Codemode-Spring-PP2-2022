import pygame as pg
from datetime import datetime

pg.init()

WIDTH = 800
HEIGHT = 600
FPS = 1

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()


image = pg.image.load('test3.png')

def blitRotate(surf, image, pos, angle):

    r_image = pg.transform.rotate(image, angle)
    rect = image.get_rect(center = pos)

    rot_rect = r_image.get_rect(center = rect.center)
    surf.blit(r_image, rot_rect)

# sec = datetime.now().strftime('%S')
sec = datetime.now().strftime('%M')
angle = int(sec) * -6
running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill((255, 255, 255))
    # r_image = pg.transform.rotate(image, angle)
    # screen.blit(image, (400, 100))

    blitRotate(screen, image, (400, 250), angle)
    sec = datetime.now().strftime('%M')
    angle = int(sec) * -6


    pg.display.update()
pg.quit()