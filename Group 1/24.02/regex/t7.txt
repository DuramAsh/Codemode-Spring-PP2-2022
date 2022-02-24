import pygame as pg 
from math import *
pg.init()

screen = pg.display.set_mode((850, 605))
pg.display.set_caption("sin & cos")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)


def draw_lines():
    # внешняя рамка
    pg.draw.rect(screen, black, [50, 15, 780, 540], 2)
    # линии
    for i in range(80, 831, 120):
        if i == 440:
            pg.draw.line(screen, black, [i, 15], [i, 555], 2)
        elif i == 560:
            pg.draw.line(screen, black, [i, 15], [i, 45], 1)
            pg.draw.line(screen, black, [i, 105], [i, 555], 1)
        else:
            pg.draw.line(screen, black, [i, 15], [i, 555], 1)
    for i in range(45, 556, 60):
        if i == 285:
            pg.draw.line(screen, black, [50, i], [830, i], 2)
        else:
            pg.draw.line(screen, black, [50, i], [830, i], 1)

def little_lines():
    # маленькие штрихи по x
    for i in range(95, 786, 30):
        pg.draw.line(screen, black, [i, 15], [i, 20], 1)
        pg.draw.line(screen, black, [i, 550], [i, 555], 1)
    for i in range(110, 771, 60):
        pg.draw.line(screen, black, [i, 15], [i, 25], 1)
        pg.draw.line(screen, black, [i, 545], [i, 555], 1)
    for i in range(140, 741, 120):
        pg.draw.line(screen, black, [i, 15], [i, 30], 1)
        pg.draw.line(screen, black, [i, 540], [i, 555], 1)
    # маленькие штрихи по y
    for i in range(60, 511, 30):
        pg.draw.line(screen, black, [50, i], [55, i], 1)
        pg.draw.line(screen, black, [825, i], [830, i], 1)
    for i in range(75, 496, 60):
        pg.draw.line(screen, black, [50, i], [60, i], 1)
        pg.draw.line(screen, black, [820, i], [830, i], 1)

def draw_sin_and_cos():
    for x in range(80, 800):
        sin_y1 = 120 * sin((x-80) / 60 * pi)
        sin_y2 = 120 * sin((x-79) / 60 * pi)
        pg.draw.aaline(screen, red, (x, 285 + sin_y1), ((x+1), 285+sin_y2))
    
    for x in range(80, 800, 2):
        cos_y1 = 240 * cos((x-80) / 120 * pi)
        cos_y2 = 240 * cos((x-81) / 120 * pi)
        pg.draw.aaline(screen, blue, (x, 285 + cos_y1), ((x-1), 285 + cos_y2))
    
def draw_nums():
    nums = ['0.00', '0.25', '0.50', '0.75', '1.00']
    myiter = iter(nums[::-1])

    font = pg.font.SysFont('times new roman', 20, False, True)
    for i in range(32, 273, 60):
        text = font.render(next(myiter), True, black)
        screen.blit(text, (11, i))

    nums.remove('0.00')
    myiter = iter(list(map(lambda x: '-' + x, nums)))

    for i in range(333, 514, 60):
        text = font.render(next(myiter), True, black)
        screen.blit(text, (4, i))

def draw_pi():
    p = chr(960)
    pikuli = ['3'+p, '2'+p, p]
    half_pikuli = ['5'+p+'/2', '3'+p+'/2', p+'/2']
    myiter = iter(half_pikuli)
    jai_iter = iter(pikuli)

    font = pg.font.SysFont('times new roman', 20, False, True)

    for i in range(140, 381, 120):
        text = font.render('-'+next(myiter), True, black)
        screen.blit(text, (i-20, 560))
    for i in range(80, 321, 120):
        text = font.render(next(jai_iter), True, black)
        screen.blit(text, (i-8, 560))
    text = font.render('0', True, black)
    text_x = font.render('X', True, black)
    screen.blit(text, (435, 560))
    screen.blit(text_x, (430, 580))

    myiter = iter(half_pikuli[::-1])
    jai_iter = iter(pikuli[::-1])

    for i in range(500, 741, 120):
        text = font.render(next(myiter), True, black)
        screen.blit(text, (i-15, 560))
    for i in range(560, 801, 120):
        text = font.render(next(jai_iter), True, black)
        screen.blit(text, (i-10, 560))
            
def sin_cos_text():
    font = pg.font.SysFont('times new roman', 25, False, False)
    sin_text = font.render('sin x', True, black)
    cos_text = font.render('cos x', True, black)
    screen.blit(sin_text, (535, 45))
    screen.blit(cos_text, (530, 70))
    pg.draw.line(screen, red, (590, 60), (640, 60), 2)
    # draw_dashed_line(screen, blue, (590, 85), (642, 85), 2)
    for x in range(590, 642, 4):
        pg.draw.line(screen, blue, (x, 85), (x, 85), 3)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(white)

    draw_lines()
    little_lines()
    draw_sin_and_cos()
    draw_nums()
    draw_pi()
    sin_cos_text()

    pg.display.update()
pg.quit()