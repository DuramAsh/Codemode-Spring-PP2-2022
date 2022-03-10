import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


FPS = 30
angle = 0
x, y = 650, 300

font = pygame.font.SysFont("Times New Roman", 18)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST PROGRAM")

finished = False

clock = pygame.time.Clock()


while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), 250, 5)
    x = WIDTH // 2 + math.cos(math.radians(angle)) * 250
    y = HEIGHT // 2 - math.sin(math.radians(angle)) * 250

    pygame.draw.line(screen, RED, (x, y), (WIDTH // 2, y), 5)
    pygame.draw.line(screen, BLUE, (x, y), (x, HEIGHT // 2), 5)
    pygame.draw.line(screen, BLACK, (WIDTH // 2 - 250, HEIGHT //
                     2), (WIDTH // 2 + 250, HEIGHT // 2), 2)
    pygame.draw.line(screen, BLACK, (WIDTH // 2, HEIGHT //
                     2 - 250), (WIDTH // 2, HEIGHT // 2 + 250), 2)
    pygame.draw.circle(screen, GREEN, (x, y), 10)

    angle += 1
    text1 = font.render(
        f"sin {angle % 360} = {math.sin(math.radians(angle)):.2f}", True, RED)
    text2 = font.render(
        f"cos {angle % 360} = {math.cos(math.radians(angle)):.2f}", True, BLUE)
    screen.blit(text1, (200, 0))
    screen.blit(text2, (200, 20))
    pygame.display.flip()

pygame.quit()
