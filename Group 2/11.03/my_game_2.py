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
game_over = font.render("GAME OVER", True, (0, 0, 0))
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Korganoid")

finished = False
lose = False
restart = True
clock = pygame.time.Clock()



def find_coor():
    coordinates = []
    for i in range(50, 350, 20):
            for j in range(50, 750, 35):
                # pygame.draw.rect(screen, BLACK, (j, i, each_block_size[1], each_block_size[0]))
                coordinates.append((j, i))
    return coordinates

while restart:
    pygame.mixer.music.play(-1)
    color_value = 0
    finished = False
    lose = False
    rect_x, rect_y = 300, 550
    rect_width, rect_height = 200, 20
    circ_x, circ_y = WIDTH // 2, HEIGHT // 2 + 200
    radius = 20
    dx, dy = randint(-5, -5), -5
    each_block_size = (15, 30)
    block_coors = find_coor()
    while not finished:
        clock.tick(FPS)
        
        coor = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = False
                finished = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and rect_x > 0:
                rect_x += -20
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and rect_x + rect_width < WIDTH:
                rect_x += 20

        screen.blit(img, (0, 0))


        pygame.draw.rect(screen, WHITE, (50, 50, 700, 300))
        #700x300
        #each_rect_size = (15, 30)
        
        for i, j in block_coors:
            pygame.draw.rect(screen, BLACK, (i, j, each_block_size[1], each_block_size[0]))
            # print(i, j)
        


        pygame.draw.circle(screen, rainbow_color(color_value), (circ_x, circ_y), radius)
        color_value = (color_value + 5) % (256 * 6)
        circ_x += dx
        circ_y += dy

        circ_bottom = (circ_x, circ_y + radius)
        if circ_x <= 0 or circ_x >= WIDTH:
            dx *= -1
        if circ_y <= 0:
            dy *= -1
        if circ_bottom[1] == rect_y and circ_bottom[0] in range(coor[0] - rect_width // 2, coor[0] + rect_width // 2 + 1):
            dx = randint(-5, 5)
            dx *= -1
            dy *= -1
        for i, j in block_coors:
            if circ_x in range(i, i + each_block_size[1]) and circ_y - radius == j + each_block_size[0]:
                block_coors.remove((i, j))
                dx = randint(-5, 5)
                dx *= -1
                dy *= -1
            elif circ_y in range(j, j + each_block_size[0]) and circ_x - radius == i + each_block_size[1]:
                block_coors.remove((i, j))
                dx = randint(-5, 5)
                dx *= -1
                dy *= -1
            elif circ_y in range(j, j + each_block_size[0]) and circ_x + radius == i:
                block_coors.remove((i, j))
                dx = randint(-5, 5)
                dx *= -1
                dy *= -1
            elif circ_x in range(i, i + each_block_size[1]) and circ_y + radius == j:
                block_coors.remove((i, j))
                dx = randint(-5, 5)
                dx *= -1
                dy *= -1

        pygame.draw.rect(screen, rainbow_color(color_value), (coor[0] - rect_width // 2, rect_y, rect_width, rect_height))
        # pygame.draw.rect(screen, WHITE, (coor[0], rect_y, rect_width, rect_height) )
        if circ_y > HEIGHT:
            lose = True
            pygame.mixer.music.stop()

        while lose:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    finished = True
                    lose = False
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 200,
                                             HEIGHT // 2 - 200, 400, 400))
            pos = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(game_over, pos)
            pygame.display.flip()
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()
