import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


FPS = 30
angle = 0

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

    pygame.draw.circle(screen, BLACK, (400, 300), 250, 5)
    # pygame.draw.circle(screen, RED, (650, 300), 20)

    pygame.display.flip()

pygame.quit()
