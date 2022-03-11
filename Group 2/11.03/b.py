import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

#Background Image
img = pygame.image.load("./img/background.jfif") # 1000x660
#Music
pygame.mixer.music.load("./music/back_mus.mp3")
pygame.mixer.music.play(-1)
#Font
font = pygame.font.Font("./font/bebas.ttf", 150)
text = font.render("Test", True, (0,0,0))

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST PROGRAM")

finished = False

clock = pygame.time.Clock()

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    # screen.fill(WHITE)
    screen.blit(img, (0, 0))
    pos = text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(text, pos)

    pygame.display.flip()
pygame.quit()
