import pygame as pg
pg.init()
# pg.mixer.init()
# pg.mixer.music.load("./music/background.mp3")
# pg.mixer.music.play(-1)
lose=False
score=0
font = pg.font.SysFont("Times New Roman", 40, True)

BLACK = (0, 0, 0)
WHITE =(255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FPS = 60
WIDTH, HEIGHT = 800, 600

pg.display.set_caption('PONG')
screen = pg.display.set_mode((WIDTH, HEIGHT))
is_running = True
clock = pg.time.Clock()
p1_x, p1_y = 20, 200
p2_x, p2_y = 700, 200
x_c, y_c, r = WIDTH//2, HEIGHT//2, 20
dx, dy = -5, 3



while is_running:
    clock.tick(FPS)
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    if keys[pg.K_w]:
        p1_y -= 3
    if keys[pg.K_s]:
        p1_y += 3          

    if keys[pg.K_UP]:
        p2_y -= 3
    if keys[pg.K_DOWN]:
        p2_y += 3
    if y_c-r <= 0:
        dy *= -1
    if y_c+r >= HEIGHT:
        dy *= -1


    ball_point = (x_c-r, y_c)

    if p1_y + 200 >= HEIGHT:
        p1_y = HEIGHT - 200
    if p1_y <= 0:
        p1_y = 0

    if p2_y + 200 >= HEIGHT:
        p2_y = HEIGHT - 200 
    if p2_y <= 0:
        p2_y = 0       

    if ball_point[1] in range(p2_y, p2_y + 200 + 1) and ball_point[0] + 2*r >= p2_x:
        dx *= -1
        score+=1
    if ball_point[1] in range(p1_y, p1_y + 200 + 1) and ball_point[0] <= p1_x + 20:
        dx *= -1       
        score+=1

    if ball_point[0] <= 0:
        lose = True
    if ball_point[0] >= WIDTH:
        lose = True    

    screen.fill(WHITE)
    pg.draw.rect(screen, BLUE, (p1_x, p1_y, 20, 200))
    pg.draw.rect(screen, GREEN, (p2_x, p2_y, 20, 200))
    pg.draw.circle(screen, RED, (x_c, y_c), r)

    x_c += dx
    y_c += dy
    while lose:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_running = False
                lose = False
            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                x_c, y_c = WIDTH // 2, HEIGHT // 2
                dx, dy = -5, 3
                r = 20
                score = 0
                pg.mixer.music.play(-1)
                lose = False
                is_running = True

        
        pg.draw.rect(screen, WHITE, (WIDTH // 2 - 200,
                     HEIGHT // 2 - 200, 400, 400))
        text1 = font.render('GAME OVER', False, False)
        text2 = font.render(f'Your score is: {score}', False, False)
        screen.blit(text1, (WIDTH // 2 - 200, HEIGHT // 2 - 200))
        screen.blit(text2, (WIDTH // 2 - 200, HEIGHT // 2 - 100))
        pg.display.flip()
    pg.display.flip()
pg.quit()