import pygame
from random import randint
pygame.init()

#Global Variables
WIDTH = 800
HEIGHT = 600

FPS = 40
#Initiliazing
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST PROGRAM")

clock = pygame.time.Clock()

finished = False
lose = False
restart = True
#Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Images
img = pygame.image.load("./img/background.png")
#Music
pygame.mixer.music.load("./music/bob.mp3")

#Font
font = pygame.font.Font("./font/bebas.ttf", 72)
text = font.render("GAME OVER", True, BLACK)
#Variables


while restart:
    # pygame.mixer.music.play(-1)
    c_x, c_y  = WIDTH // 2, HEIGHT // 2 + 200
    r_x, r_y = WIDTH // 2, HEIGHT // 2 + 250
    r_width, r_height = 200, 30
    dx, dy = 5, -5
    step = 10
    RAD = 10
    control_mode = -1
    finished = False
    lose = False
    while not finished:
        clock.tick(FPS)
        # m_pos = pygame.mouse.get_pos()

        keydowns = pygame.key.get_pressed()

        c_pos = (c_x, c_y + RAD)

        screen.blit(img, (0, 0))
        # screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = False
                finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.mixer.music.stop()
                if event.key == pygame.K_m:
                    pygame.mixer.music.play(-1)
                if event.key == pygame.K_s:
                    step += 2
                if event.key == pygame.K_c:
                    control_mode *= -1

        
            
        if control_mode == 1:
            m_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_focused() == 0:
                if m_pos[0]  < WIDTH // 2:
                    r_x = r_width // 2
                else:
                    r_x = WIDTH - r_width // 2
            else:
                r_x = m_pos[0]

        if keydowns[pygame.K_LEFT] and r_x - r_width // 2 > 0 and control_mode == -1:
            r_x -= step
        elif keydowns[pygame.K_RIGHT] and r_x + r_width // 2 < WIDTH and control_mode == -1:
            r_x += step

        if c_y <= 0:
            dy *= -1
        if c_x <= 0 or c_x >= WIDTH:
            dx *= -1
        # if c_pos[1] == r_y ----- c_pos[1] == 600 ???
        if c_pos[1] in range(r_y, r_y + 5) and c_pos[0] in range(r_x - r_width // 2, r_x + r_width // 2 + 1):
            dy *= -1 
            # c_pos[1] > r_y and c_pos[1] < r_y + 10

        c_x += dx
        c_y += dy

        pygame.draw.circle(screen, RED, (c_x, c_y), RAD)

        pygame.draw.rect(screen, BLUE, (r_x - r_width // 2, r_y, r_width, r_height))
        
        if c_y - RAD > HEIGHT:
            lose = True
            pygame.mixer.music.stop()

        while lose:
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 250, HEIGHT // 2 - 200, 500, 400))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    lose = False
                    finished = True

            screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
            
            pygame.display.flip()

        pygame.display.flip()

    pygame.display.flip()
pygame.quit()