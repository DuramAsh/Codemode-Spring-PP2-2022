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
PURPLE = (221,160,221)
#Images
img = pygame.image.load("./img/background.png")
#Music
pygame.mixer.music.load("./music/bob.mp3")

#Font
font = pygame.font.Font("./font/bebas.ttf", 72)
lil_font = pygame.font.Font("./font/bebas.ttf", 24)
game_over = font.render("GAME OVER", True, BLACK)
win_over = font.render("YOU WON!", True, BLACK)
#Variables
area = (700, 300)
each = (33, 18)

def find_pos():
    positions = []
    for i in range(50, area[0] + 50, 35):
            for j in range(50, area[1] + 50, 20):
                # pygame.draw.rect(screen, BLACK, (i, j, each[0], each[1]))
                positions.append((i, j))
    return positions

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
    win = False
    positions = find_pos()
    SCORE = 0
    while not finished:
        clock.tick(FPS)
        # m_pos = pygame.mouse.get_pos()

        keydowns = pygame.key.get_pressed()

        c_pos = (c_x, c_y + RAD)

        screen.fill(PURPLE)
        # screen.blit(img, (0, 0))

        pygame.draw.rect(screen, WHITE, (50, 50, area[0], area[1]))

        for x, y in positions:
            pygame.draw.rect(screen, BLACK, (x, y, each[0], each[1]))
            if c_y - RAD in range(y + each[1] - 3, y + each[1] + 2) and c_x in range(x, x + each[0] + 1):
                if dy < 0:
                    dy = randint(5, 10)
                else:
                    dy = randint(-10, -5)
                positions.remove((x, y))
                SCORE += 1
            elif c_y + RAD in range(y - 3, y + 2) and c_x in range(x, x + each[0] + 1):
                if dy < 0:
                    dy = randint(5, 10)
                else:
                    dy = randint(-10, -5)
                positions.remove((x, y))
                SCORE += 1
            elif c_x - RAD in range(x + each[0] - 3, x + each[0] + 2) and c_y in range(y, y + each[1]):
                if dx < 0:
                    dx = randint(5, 10)
                else:
                    dx = randint(-10, -5)
                positions.remove((x, y))
                SCORE += 1
            elif c_x + RAD in range(x - 3, x + 2) and c_y in range(y, y + each[1]):
                if dx < 0:
                    dx = randint(5, 10)
                else:
                    dx = randint(-10, -5)
                positions.remove((x, y))
                SCORE += 1

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
        if c_pos[1] in range(r_y - 5, r_y + 5) and c_pos[0] in range(r_x - r_width // 2, r_x + r_width // 2 + 1):
            if dy < 0:
                dy = randint(5, 10)
            else:
                dy = randint(-10, -5) 
            # c_pos[1] > r_y and c_pos[1] < r_y + 10

        c_x += dx
        c_y += dy

        pygame.draw.circle(screen, RED, (c_x, c_y), RAD)

        pygame.draw.rect(screen, BLUE, (r_x - r_width // 2, r_y, r_width, r_height))
        
        score_text = lil_font.render(f'Score: {SCORE}', True, RED)
        screen.blit(score_text, (10, HEIGHT - 50))

        if len(positions) == 0:
            win = True

        if c_y - RAD > HEIGHT:
            lose = True
            pygame.mixer.music.stop()

        while lose or win:
            total_score = font.render(f'Score: {SCORE}', True, BLUE)
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 250, HEIGHT // 2 - 200, 500, 400))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                    win = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    lose = False
                    finished = True
                    win = False

            if lose:
                pos = game_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))
                screen.blit(game_over, (pos[0], pos[1] - 50))
            elif win:
                pos = win_over.get_rect(center = (WIDTH // 2, HEIGHT // 2))
                screen.blit(win_over, (pos[0], pos[1] - 50))
            
            pos_2 = total_score.get_rect(center = (WIDTH // 2, HEIGHT // 2))
            screen.blit(total_score, (pos_2[0], pos_2[1] + 80))
            
            
            pygame.display.flip()

        pygame.display.flip()

    pygame.display.flip()
pygame.quit()