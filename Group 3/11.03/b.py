import pygame
from random import randint
pygame.init()

#Global Variables
WIDTH, HEIGHT = 800, 600
FPS = 30
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Test")

clock = pygame.time.Clock()

finished = False
#Variables
circ_x, circ_y = WIDTH // 2, HEIGHT // 2
RAD = 40
dx, dy = 0, 0
step = 5
color = RED
while not finished:
    clock.tick(FPS)

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and circ_x + RAD < WIDTH:
                dx = step
                dy = 0
            if event.key == pygame.K_LEFT and circ_x - RAD > 0:
                dx = -step
                dy = 0
            if event.key == pygame.K_UP and circ_y - RAD > 0:
                dy = -step
                dx = 0
            if event.key == pygame.K_DOWN and circ_y + RAD < HEIGHT:
                dy = step
                dx = 0
            if event.key == pygame.K_SPACE:
                color = (randint(0, 255), randint(0, 255), randint(0, 255))

    circ_x += dx
    circ_y += dy
    
    pygame.draw.circle(screen, color, (circ_x, circ_y), RAD)

    pygame.display.flip()
pygame.quit()