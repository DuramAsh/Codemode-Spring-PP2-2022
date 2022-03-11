import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLOR = BLUE


FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST PROGRAM")

finished = False

x, y = WIDTH // 2, HEIGHT // 2
radius = 30
dx, dy = 0, 0
acceleration = 1
# new_var or +FPS
clock = pygame.time.Clock()

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            dy = -acceleration
            dx = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            dy = acceleration
            dx = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            dx = -acceleration
            dy = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            dx = acceleration
            dy = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if dx == 0 and dy == 0:
                acceleration += 1
            elif dy == 0 and dx != 0:
                acceleration += 1
                dx = acceleration
            elif dx == 0 and dy != 0:
                acceleration += 1
                dy = acceleration
            # dx = acceleration
            # dy = acceleration
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            COLOR = (random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255))

    screen.fill(WHITE)
    COLOR = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    pygame.draw.circle(screen, COLOR, (x, y), radius)

    x += dx
    y += dy

    pygame.display.flip()
pygame.quit()
