import pygame as pg
pg.init()
pg.display.set_caption("AIBERGENOID")

pg.mixer.init()
pg.mixer.music.load("./music/background.mp3")
pg.mixer.music.play(-1)

WIDTH = 800
HEIGHT = 600
FPS = 60

background_img = pg.image.load("./images/background.png")
background_img = pg.transform.scale(background_img, (WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

x_c, y_c = WIDTH // 2, HEIGHT - 100
dx, dy = 4, -6
r = 30

running = True

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    screen.fill(WHITE)
    screen.blit(background_img, (0, 0))
    
    pg.draw.circle(screen, RED, (x_c, y_c), r)
    
    if x_c + r >= WIDTH or x_c - r <= 0:
        dx *= -1
    if y_c - r <= 0:
        dy *= -1
    
    x_c += dx
    y_c += dy
    
    (x_r, y_r) = pg.mouse.get_pos()
    pg.draw.rect(screen, BLUE, (x_r - 200, 500, 400, 20))
    
    pg.display.flip()
pg.quit()


# Sharik + 
# Kolliziya s granitsami +
# Shtuka vnizu 
# Dvigat' shtuku vnizu
# Kolliziya sharika so shtukoy vnizu