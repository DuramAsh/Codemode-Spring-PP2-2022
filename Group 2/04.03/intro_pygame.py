import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 15

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("TEST WINDOW")

finished = False

clock = pygame.time.Clock()

while not finished:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
    screen.fill(WHITE)
    
    
    
    clock.tick(FPS)	
    pygame.display.flip()

pygame.quit()