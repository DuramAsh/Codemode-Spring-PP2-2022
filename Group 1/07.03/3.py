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
rotation = 0

while is_running:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
    screen.fill(WHITE)
    
    
    
    font2 = pg.font.SysFont("Times New Roman", 60, True, False)
    
    text2 = font2.render("IMA ROTATIN", True, BLACK)
    text2 = pg.transform.rotate(text2, rotation)
    rotation += 1
    screen.blit(text2, (30, 160))
    
    
    
    
    pg.display.flip()
pg.quit()