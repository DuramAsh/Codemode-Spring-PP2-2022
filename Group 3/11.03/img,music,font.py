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
#Color
BLACK = (0, 0, 0)
#Images
img = pygame.image.load("./img/background.png")
#Music
pygame.mixer.music.load("./music/bob.mp3")
pygame.mixer.music.play(-1)
#Font
font = pygame.font.Font("./font/bebas.ttf", 150)
text = font.render("LOL", True, BLACK)
while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pygame.mixer.music.stop()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            pygame.mixer.music.play(-1)

    screen.blit(img, (0, 0)) # Surfaces: rendered(string), pygame.figures, images
    screen.blit(text, (WIDTH // 2, HEIGHT // 2))
    
    pygame.display.flip()
pygame.quit()