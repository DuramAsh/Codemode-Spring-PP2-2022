import pygame
pygame.init()

#Global Variables
WIDTH = 800
HEIGHT = 600

FPS = 20
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Initiliazing
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST PROGRAM")

clock = pygame.time.Clock()

finished = False
move = 0
while not finished:
    clock.tick(FPS)

    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    
    
    pygame.draw.line(screen, BLACK, (WIDTH // 4, (HEIGHT // 2 + move) % HEIGHT), (WIDTH * 3 // 4, (HEIGHT // 2 + move) % HEIGHT), 10)
    move += 5
    
    pygame.display.flip()
pygame.quit()