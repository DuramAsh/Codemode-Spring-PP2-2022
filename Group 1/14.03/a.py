import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()

running = 1

x = 400
y = 300

while running:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = 0
        
        
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x -= 3
    if keys[pg.K_RIGHT]:
        x += 3
    if keys[pg.K_DOWN]:
        y += 3
    if keys[pg.K_UP]:
        y -= 3
            

    screen.fill((255, 255, 255))


    pg.draw.circle(screen, (0, 0, 0), (x, y), 20)
    pg.display.flip()

pg.quit()
