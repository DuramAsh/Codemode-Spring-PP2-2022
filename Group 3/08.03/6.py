import pygame, math
pygame.init()
#GLOBAL variables
WIDTH, HEIGHT = 800, 600
FPS = 20
RAD = 250
angle = 0

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Initializing
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beta DVD")

clock = pygame.time.Clock()

finished = False



while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    screen.fill(WHITE)

    x = WIDTH // 2 + math.cos(math.radians(angle)) * RAD
    y = HEIGHT // 2 + math.sin(math.radians(angle)) * RAD

    angle += 1

    pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), RAD, 5)

    pygame.draw.circle(screen, RED, (x, y), 15)


    pygame.display.flip()
pygame.quit()