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

font = pygame.font.SysFont("Times New Roman", 60, False, False)
text = font.render("CodeMode", True, BLACK)

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    screen.fill(WHITE)

    screen.blit(text, (50, 50))
    
    textRotated1 = pygame.transform.rotate(text, 90)
    textRotated2 = pygame.transform.rotate(text, 180)
    textRotated3 = pygame.transform.rotate(text, 270)

    screen.blit(textRotated1, (50, 150))
    screen.blit(textRotated2, (350, 50))
    screen.blit(textRotated3, (100, 150))

    pygame.display.flip()
pygame.quit()