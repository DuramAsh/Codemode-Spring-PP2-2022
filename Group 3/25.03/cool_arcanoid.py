import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 45

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('"OOP" Arcanoid')

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)


restart = True

while restart:
    finished = False
    lose = False
    win = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = False
                finished = True
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            #     lose = True

        screen.fill(PURPLE)


        while lose or win:
            pygame.draw.rect(screen, WHITE, (150, 100, 500, 400))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                    win = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    lose = False
                    win = False
                    finished = True


            pygame.display.flip()
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()