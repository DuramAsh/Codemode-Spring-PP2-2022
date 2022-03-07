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
    
    font = pg.font.Font(None, 50)
    text1 = font.render("Welcome", True, GREEN)
    
    screen.blit(text1, (30, 70))
    
    font2 = pg.font.SysFont("Times New Roman", 60, True, False)
    
    text2 = font2.render("hello", True, BLACK)
    screen.blit(text2, (30, 160))
    
    text2_rotated = pg.transform.rotate(text2, 90)
    screen.blit(text2_rotated, (200, 160))
    
    text3_rotated = pg.transform.rotate(text2, 180)
    screen.blit(text3_rotated, (300, 160))
    
    text4_rotated = pg.transform.rotate(text2, 270)
    screen.blit(text4_rotated, (500, 160))
    
    
    pg.display.flip()
pg.quit()