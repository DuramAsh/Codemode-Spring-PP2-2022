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

font = pg.font.SysFont("Times New Roman", 40, True)

x_c, y_c = WIDTH // 2, HEIGHT - 150
dx, dy = -4, -6
r = 30
score = 0
x = 0

running = True
lose = False
mouse = False

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                mouse = not mouse


    screen.fill(WHITE)
    screen.blit(background_img, (0, 0))

    pg.draw.circle(screen, RED, (x_c, y_c), r)
    
    keys = pg.key.get_pressed()
    # if mouse:
    #     (x, y_r) = pg.mouse.get_pos()
        
    if keys[pg.K_LEFT]:
        x -= 3
    elif keys[pg.K_RIGHT]:
        x += 3
            

    if x_c + r >= WIDTH or x_c - r <= 0:
        dx *= -1
        score += 1
    if y_c - r <= 0:
        dy *= -1
        score += 1

    x_c += dx
    y_c += dy

    
    if x <= 200:
        x = 200
    if x >= 600:
        x = 600

    if y_c >= HEIGHT:
        lose = True
        pg.mixer.music.stop()

    pg.draw.rect(screen, BLUE, (x - 200, 500, 400, 20))

    ball_point = (x_c, y_c + r)
    # Collision of ball with blue thing
    if (ball_point[0] in range(x - 200, x + 200 + 1)) and (ball_point[1] >= 500):
        dy *= -1
        score += 1

    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                lose = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    x_c, y_c = WIDTH // 2, HEIGHT - 150
                    dx, dy = 4, -6
                    r = 30
                    score = 0
                    pg.mixer.music.play(-1)
                    lose = False
                    running = True

        
        pg.draw.rect(screen, WHITE, (WIDTH // 2 - 200,
                     HEIGHT // 2 - 200, 400, 400))
        text1 = font.render('GAME OVER', False, False)
        text2 = font.render(f'Your score is: {score}', False, False)
        screen.blit(text1, (WIDTH // 2 - 200, HEIGHT // 2 - 200))
        screen.blit(text2, (WIDTH // 2 - 200, HEIGHT // 2 - 100))
        pg.display.flip()
    pg.display.flip()
pg.quit()


# Sharik +
# Kolliziya s granitsami +
# Shtuka vnizu +
# Dvigat' shtuku vnizu +
# Kolliziya sharika so shtukoy vnizu +