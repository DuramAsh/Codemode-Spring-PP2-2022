import pygame 
pygame.init()

#GLOBAL variables
WIDTH, HEIGHT = 800, 600
FPS = 20

#Initiliazing
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


#Variables
finished = False
move = 0

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#pygame.Rect
#pygame.Surface

rect_1 = pygame.Rect(100, 100, 50, 50)
rect_2 = pygame.Rect(300, 300, 50, 50)
#x, y, width, height


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill(BLACK)

    # pygame.draw.rect(screen, WHITE, (r_x, r_y, 400, 400))
    pygame.draw.rect(screen, WHITE, (rect_1))
    pygame.draw.rect(screen, RED, (rect_2))
    rect_1.move_ip(1, 1)

    if rect_1.colliderect(rect_2):
        finished = True

    

    #RBG(#, #, #)
    #RGBA(#, #, #, прозрачность)

    pygame.display.flip()
pygame.quit()