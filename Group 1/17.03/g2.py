from turtle import width
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

# Initializing 
WIDTH = 800
HEIGHT = 600
FPS = 30

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Background

# Music

# Font
font = pygame.font.Font("./font/bebas.ttf", 72)
game_over = font.render("GAME OVER", True, BLACK)
player1 = font.render("Player 1 WON!", True, BLACK)
player2 = font.render("Player 2 WON!", True, BLACK)

# Set
finished = False
lose = False
win = False
restart = True

# Clock
clock = pygame.time.Clock()

while restart:
    # pygame.mixer.music.play(-1)

    # Start / Win / Lose
    finished = False
    win = False
    lose = False

    # Rectangles
    rect_x1, rect_y1 = 30, 200
    rect_x2, rect_y2 = 750, 200
    rect_width, rect_height = 20, 200

    # Circle
    circ_x, circ_y = WIDTH // 2, HEIGHT // 2 + 200
    radius = 10
    dx, dy = -5, -5
    color_value = 0

    # Scores 
    score1 = 0
    score2 = 0
    total = 5

    while not finished:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                restart = False
        screen.fill((WHITE))
        
        keydowns1 = pygame.key.get_pressed()
        if keydowns1[pygame.K_UP] and rect_y1 // 2 > 0:
            rect_y1 += -20
        if keydowns1[pygame.K_DOWN] and rect_y1 + rect_height < HEIGHT:
            rect_y1 += 20
        
        if keydowns1[pygame.K_w] and rect_y2 // 2 > 0:
            rect_y2 += -20
        if keydowns1[pygame.K_s] and rect_y2 + rect_height < HEIGHT:
            rect_y2 += 20

        pygame.draw.circle(screen, rainbow_color(color_value), (circ_x, circ_y), radius)
        color_value = (color_value + 5) % (256 * 6)
        circ_x += dx
        circ_y += dy

        circ_bottom = (circ_x, circ_y + radius)
        if circ_y <= 0 or circ_y >= HEIGHT:
            dy *= -1
        
        # For left block
        if (circ_x) <= rect_x1 + rect_width and (circ_y) in range(rect_y1, rect_y1 + rect_height):
            if dx < 0:
                dx = randint(5, 10)
            else:
                dx = randint(-10, -5)

        # For right block
        if (circ_x) >= rect_x2 and (circ_y) in range(rect_y2, rect_y2 + rect_height):
            if dx > WIDTH:
                dx = randint(5, 10)
            else:
                dx = randint(-10, -5)

        if circ_x == 0:
            score2 += 1
        elif circ_x == WIDTH:
            score1 += 1

        if circ_x <= 0 or circ_x >= WIDTH:
            circ_x = WIDTH // 2
            circ_y = HEIGHT // 2
        
        if score1 == total:
            game_over.set_colorkey((255, 255, 255))
            pos = game_over.get_rect(center = (WIDTH // 2 - 20, HEIGHT // 2))
            screen.blit(player1, pos)
        if score1 == total:
            game_over.set_colorkey((255, 255, 255))
            pos = game_over.get_rect(center = (WIDTH // 2 - 20, HEIGHT // 2))
            screen.blit(player2, pos)


        pygame.draw.rect(screen, BLUE, (rect_x1, rect_y1, rect_width, rect_height))
        pygame.draw.rect(screen, BLUE, (rect_x2, rect_y2, rect_width, rect_height))
        
        pygame.display.flip()

pygame.quit()