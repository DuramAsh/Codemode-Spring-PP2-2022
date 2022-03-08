import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


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
    pygame.draw.circle(screen, RED, (x, y), 20)

    x = WIDTH // 2 + math.cos(math.radians(angle)) * 250
    y = HEIGHT // 2 - math.sin(math.radians(angle)) * 250

    angle += 1
    text = font.render(f"sin {angle % 360} = {math.sin(math.radians(angle))}", True, RED)
    screen.blit(text, (200, 0))
    pygame.display.flip()

pygame.quit()
