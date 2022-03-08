import pygame
from random import randint

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 30  # Количество циклов в 1 секунде

# Создание окна с размерами (WIDTH, HEIGHT)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST PROGRAM")  # Название вашего окна

finished = False  # для цикла

clock = pygame.time.Clock()  # для контроля количества циклов

x, y = 50, 50
# dx, dy = randint(5, 15), randint(5, 15)
dx, dy = 8, 5

while not finished:
    clock.tick(FPS)  # задаем значения количеству циклов

    for event in pygame.event.get():  # отслеживание всех действий
        if event.type == pygame.QUIT:  # для закрытия окна
            finished = True

    x += dx
    y += dy

    screen.fill(WHITE)  # заливка

    # pygame.draw.line(переменная за экран, цвет, старт_координата, энд_координата, толщина)
    pygame.draw.rect(screen, BLACK, (x, y, 100, 100))
    
    if x + 100 == WIDTH or x == 0:
        dx *= (-1)
    if y + 100 == HEIGHT or y == 0:
        dy *= (-1)

    pygame.display.flip()  # отображаем изменения на экране

pygame.quit()
