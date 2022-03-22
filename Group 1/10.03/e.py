# space button
# квадрат бьется об стенку, отражается, и меняет цвет при нажатии на пробел
import pygame as pg
import random

pg.init()
pg.display.set_caption("Square changes color")
WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

rect_x, rect_y = 70, 70
dx, dy = 3, 3
x = 300
y = 150
color = RED
font = pg.font.SysFont("Times New Roman", 60, True, True) # шрифт, размер шрифта, жирный, курсив

running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
        #     y += dy

    keys = pg.key.get_pressed()

    if(keys[pg.K_DOWN]):
        y += dy

    if y + 70 >= HEIGHT:
        dy = 0

    pg.draw.rect(screen, color, (x, y, rect_x, rect_y))
    # x += dx
    text1 = font.render('Aruzhan', True, (255, 0, 0), (0, 255, 0)) # text, сглаживание, цвет шрифта, цвет фона

    screen.blit(text1, (100, 100))
    


    pg.display.flip()
pg.quit()
