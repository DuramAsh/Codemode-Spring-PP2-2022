import pygame
pygame.init()

#Global Variables
WIDTH = 800
HEIGHT = 600

FPS = 20
#Initiliazing
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST PROGRAM")

clock = pygame.time.Clock()

finished = False
while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    
    pygame.display.flip()
pygame.quit()