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

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Korganoid")

finished = False
clock = pygame.time.Clock()

rect_x, rect_y = 300, 550

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.blit(img, (0, 0))
    pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2 + 200), 20)
    pygame.draw.rect(screen, GREEN, (rect_x, rect_y, 200, 20))

    pygame.display.flip()
pygame.quit()