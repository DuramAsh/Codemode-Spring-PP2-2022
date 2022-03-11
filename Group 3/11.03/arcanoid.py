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
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#Images
img = pygame.image.load("./img/background.png")
#Music
pygame.mixer.music.load("./music/bob.mp3")
pygame.mixer.music.play(-1)
#Font
font = pygame.font.Font("./font/bebas.ttf", 150)
text = font.render("LOL", True, BLACK)
#Variables
c_x, c_y  = WIDTH // 2, HEIGHT // 2 + 200
r_x, r_y = WIDTH // 2, HEIGHT // 2 + 250
r_width, r_height = 200, 30
RAD = 30

while not finished:
    clock.tick(FPS)
    m_pos = pygame.mouse.get_pos()

    # screen.blit(img, (0, 0))
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.stop()
            if event.key == pygame.K_m:
                pygame.mixer.music.play(-1)

    pygame.draw.circle(screen, RED, (c_x, c_y), RAD)

    pygame.draw.rect(screen, BLUE, (m_pos[0] - r_width // 2, r_y, r_width, r_height))
    
    
    pygame.display.flip()
pygame.quit()