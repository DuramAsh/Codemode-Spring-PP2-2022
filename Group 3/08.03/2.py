import pygame
pygame.init()
#GLOBAL variables
WIDTH, HEIGHT = 800, 600
FPS = 30

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

    font = pygame.font.SysFont("Times New Roman", 60, False, False)
    
    text = font.render("CodeMode", True, BLACK)

    screen.blit(text, (50, 50))

    pygame.display.flip()
pygame.quit()