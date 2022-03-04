import pygame
pygame.init()

#Global Variables
WIDTH = 800
HEIGHT = 600
FPS = 60

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#Initializing
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST WINDOW")

font = pygame.font.SysFont('times-new-roman', 20)

finished = False

clock = pygame.time.Clock()

#Text Rendering
text_1 = font.render('CodeMODE', False, RED)

#Coordinates
CENTER = (WIDTH // 2 - 50, HEIGHT // 2)

x = 0

while not finished:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
     
    screen.fill(WHITE)
    
    pygame.draw.line(screen, BLACK, (WIDTH // 4, (HEIGHT // 2 + x) % HEIGHT), (WIDTH * 3 // 4, (HEIGHT // 2 + x) % HEIGHT), 5) 
    x += 5
    screen.blit(text_1, CENTER)
    
    clock.tick(FPS)	
    pygame.display.flip()

pygame.quit()