import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# font = pygame.font.Font(None, 50)
font = pygame.font.SysFont("Times New Roman", 50, False, False)

FPS = 30  # Количество циклов в 1 секунде
angle = 0

# Создание окна с размерами (WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST PROGRAM")  # Название вашего окна

finished = False  # для цикла

clock = pygame.time.Clock()  # для контроля количества циклов


while not finished:
    clock.tick(FPS)  # задаем значения количеству циклов

    for event in pygame.event.get():  # отслеживание всех действий
        if event.type == pygame.QUIT:  # для закрытия окна
            finished = True

    screen.fill(WHITE)  # заливка

    text1 = font.render("HELLO", True, RED)
    rotated_text1 = pygame.transform.rotate(text1, 90)
    screen.blit(text1, (200, 200))
    # text2 = font.render("HELLO", False, RED)
    # screen.blit(text2, (200, 300))

    pygame.display.flip()  # отображаем изменения на экране

pygame.quit()
