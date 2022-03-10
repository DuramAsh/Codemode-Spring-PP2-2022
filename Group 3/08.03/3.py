import pygame
pygame.init()
#GLOBAL variables
WIDTH, HEIGHT = 800, 600
FPS = 30

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Initializing
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beta DVD")

clock = pygame.time.Clock()

finished = False

font = pygame.font.SysFont("Times New Roman", 60, False, False)
font_for_little_texts = pygame.font.SysFont("Helvetica",30, False, True)
font_from_inet = pygame.font.Font("./font/Tisa Sans Pro Light.ttf", 150)

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    screen.fill(WHITE)

    
    
    text = font.render("CodeMode", True, BLACK)

    title = font_for_little_texts.render("Fonts", True, RED)

    internet = font_from_inet.render("Tisa", True, BLUE)

    screen.blit(text, (250, 50))
    screen.blit(title, (250, 150))
    screen.blit(internet, (300,300))

    pygame.display.flip()
pygame.quit()