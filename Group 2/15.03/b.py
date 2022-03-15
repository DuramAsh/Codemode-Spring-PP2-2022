import pygame
from random import randint

pygame.init()

def rainbow_color(value):
    step = (value // 256) % 6
    pos = value % 256

    if step == 0:
        return (255, pos, 0)
    if step == 1:
        return (255-pos, 255, 0)
    if step == 2:
        return (0, 255, pos)
    if step == 3:
        return (0, 255-pos, 255)
    if step == 4:
        return (pos, 0, 255)
    if step == 5:
        return (255, 0, 255-pos)

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Background Image
img = pygame.image.load("./img/background.jfif")  # 1000x660
# Music
pygame.mixer.music.load("./music/back_mus.mp3")

# Font
font = pygame.font.Font("./font/bebas.ttf", 72)
font_lil = pygame.font.Font("./font/bebas.ttf", 24)
game_over = font.render("GAME OVER", True, BLACK)
win_over = font.render("YOU WON!", True, BLACK)
FPS = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Korganoid")

finished = False
lose = False
restart = True
clock = pygame.time.Clock()

# Variables
area = (700, 300)
each_block = (30, 15)

def find_pos():
    positions = []
    for i in range(50, area[0] + 50, 35):
            for j in range(50, area[1] + 50, 20):
                positions.append((i, j))
                # pygame.draw.rect(screen, BLACK, (i, j, each_block[0], each_block[1]))
    return positions

while restart:
    pygame.mixer.music.play(-1)
    pygame.mouse.set_visible(0)
    color_value = 0
    finished = False
    lose = False
    win = False
    rect_x, rect_y = 300, 550 
    rect_width, rect_height = 200, 20
    circ_x, circ_y = WIDTH // 2, HEIGHT // 2 + 200
    radius = 10
    dx, dy = -5, -5
    control_mode = 0
    positions = find_pos()
    SCORE = 0
    
    while not finished:
        clock.tick(FPS)
        
        m_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = False
                finished = True
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and rect_x > 0:
            #     rect_x += -20
            # if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and rect_x + rect_width < WIDTH:
            #     rect_x += 20
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                rect_x = m_pos[0]
                control_mode = 1


        keydowns = pygame.key.get_pressed()
        if keydowns[pygame.K_LEFT] and rect_x - rect_width // 2 > 0 and control_mode == 0:
            rect_x += -20
        elif keydowns[pygame.K_RIGHT] and rect_x + rect_width // 2 < WIDTH and control_mode == 0:
            rect_x += 20

        if control_mode == 1:
            if (m_pos[0] - rect_width // 2 > 0 and m_pos[0] + rect_width // 2 < WIDTH):
                rect_x = m_pos[0]
            elif pygame.mouse.get_focused() == 0:
                if m_pos[0] < WIDTH // 2:
                    rect_x  =  rect_width // 2
                elif m_pos[0] > WIDTH // 2:
                    rect_x = WIDTH - rect_width // 2
        


        screen.blit(img, (0, 0))

        # pygame.draw.rect(screen, WHITE, (50, 50, area[0], area[1]))

        for x, y in positions:
            pygame.draw.rect(screen, BLACK, (x,y, each_block[0], each_block[1]))

            if (circ_y - radius) in range(y + each_block[1] - 5, y + each_block[1] + 2) and circ_x in range(x, x + each_block[0]):
                positions.remove((x, y))
                if dy < 0:
                    dy = randint(5, 10)
                else:
                    dy = randint(-10, -4)
                SCORE += 1
            elif (circ_y + radius) in range(y - 1, y + 3) and circ_x in range(x, x + each_block[0]):
                positions.remove((x, y))
                if dy < 0:
                    dy = randint(5, 10)
                else:
                    dy = randint(-10, -4)
                SCORE += 1
            elif circ_x - radius in range(x + each_block[0] - 4, x + each_block[0] + 2) and circ_y in range(y, y+ each_block[1]):
                positions.remove((x, y))
                if dx < 0:
                    dx = randint(5, 10)
                else:
                    dx = randint(-10, -4)
                SCORE += 1
            elif circ_x + radius in range(x - 4, x + 2) and circ_y in range(y, y+ each_block[1]):
                positions.remove((x, y))
                if dx < 0:
                    dx = randint(5, 10)
                else:
                    dx = randint(-10, -4)
                SCORE += 1
            
                
                


        pygame.draw.circle(screen, rainbow_color(color_value), (circ_x, circ_y), radius)
        color_value = (color_value + 5) % (256 * 6)
        circ_x += dx
        circ_y += dy

        circ_bottom = (circ_x, circ_y + radius)
        if circ_x <= 0 or circ_x >= WIDTH:
            dx *= -1
        if circ_y <= 0:
            dy *= -1
        if (circ_y + radius) in range(rect_y - 10, rect_y + 10) and circ_bottom[0] in range(rect_x - rect_width // 2, rect_x + rect_width // 2 + 1):
            if dy < 0:
                dy = randint(5, 10)
            else:
                dy = randint(-10, -4)

        pygame.draw.rect(
                screen, rainbow_color(color_value), (rect_x - rect_width // 2, rect_y, rect_width, rect_height))
        
        score_text = font_lil.render(f'Score: {SCORE}', True, WHITE)
        screen.blit(score_text, (10, HEIGHT - 50))

        if circ_y > HEIGHT:
            lose = True
            pygame.mixer.music.stop()
        if len(positions) == 0:
            win = True

        while lose or win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                    win = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    finished = True
                    lose = False
                    win = False
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 200,
                                             HEIGHT // 2 - 200, 400, 400))
            if lose:
                pos = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(game_over, pos)
            elif win:
                pos = win_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                screen.blit(win_over, pos)
            
            total_score = font.render(f"Score: {SCORE}", True, BLACK)
            pos_2 = total_score.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(total_score, (pos_2[0], pos_2[1] + 80))
            pygame.display.flip()
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()
