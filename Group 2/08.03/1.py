import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

FPS = 30 # Количество циклов в 1 секунде

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Создание окна с размерами (WIDTH, HEIGHT)
pygame.display.set_caption("TEST PROGRAM") # Название вашего окна

finished = False # для цикла

clock = pygame.time.Clock() # для контроля количества циклов

while not finished:
    clock.tick(FPS) # задаем значения количеству циклов

    for event in pygame.event.get(): # отслеживание всех действий
        if event.type == pygame.QUIT: # для закрытия окна
            finished = True

    screen.fill(WHITE) # заливка

    pygame.draw.line(screen, BLACK, (WIDTH // 4, HEIGHT // 2), (WIDTH * 3 // 4, HEIGHT // 2), 5)
    #pygame.draw.line(переменная за экран, цвет, старт_координата, энд_координата, толщина)

    pygame.display.flip() # отображаем изменения на экране
    
pygame.quit()