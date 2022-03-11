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
rect_width, rect_height = 200, 20
circ_x, circ_y = WIDTH // 2, HEIGHT // 2 + 200
radius = 20
dx, dy = -2, -5

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and rect_x > 0:
            rect_x += -20
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and rect_x + rect_width < WIDTH:
            rect_x += 20
        

    screen.blit(img, (0, 0))
    pygame.draw.circle(screen, RED, (circ_x, circ_y), radius)
    circ_x += dx
    circ_y += dy
    
    circ_bottom = (circ_x, circ_y + radius)
    if circ_x <= 0 or circ_x >= WIDTH:
        dx *= -1
    if circ_y <= 0:
        dy *= -1
    if circ_bottom[1] == rect_y and circ_bottom[0] in range(rect_x, rect_x + rect_width + 1):
        dy *= -1
        
    

    pygame.draw.rect(screen, GREEN, (rect_x, rect_y, rect_width, rect_height))


    pygame.display.flip()
pygame.quit()
