import pygame, math
pygame.init()
#GLOBAL variables
WIDTH, HEIGHT = 800, 600
FPS = 30
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
pygame.display.set_caption("Sin and Cos")

clock = pygame.time.Clock()

finished = False

font = pygame.font.SysFont("Times New Roman", 18, True)


while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    screen.fill(WHITE)

    x = WIDTH // 2 + math.cos(math.radians(angle)) * RAD
    y = HEIGHT // 2 - math.sin(math.radians(angle)) * RAD

    angle += 1

    pygame.draw.circle(screen, BLACK, (WIDTH // 2, HEIGHT // 2), RAD, 5)

    pygame.draw.circle(screen, RED, (x, y), 15)

    sinus = font.render(f'sin({angle % 360}): {math.sin(math.radians(angle)):.3f}', True, RED)
    screen.blit(sinus, (200, 25))


    pygame.display.flip()
pygame.quit()