import pygame as pg
from random import randint

WIDTH = 800
HEIGHT = 800
FPS = 24
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Snake:
    def __init__(self):
        self.length = 1
        self.color = RED
        self.score = 0
        self.body = [[100, 100]]
        self.dx = 5
        self.dy = 0

    def move(self):

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.dx = -5
            self.dy = 0
        if keys[pg.K_d]:
            self.dx = 5
            self.dy = 0
        if keys[pg.K_w]:
            self.dy = -5
            self.dx = 0
        if keys[pg.K_s]:
            self.dy = 5
            self.dx = 0

        for part in range(self.length - 1, 0, -1):
            self.body[part][0] = self.body[part - 1][0]
            self.body[part][1] = self.body[part - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (part[0], part[1], 40, 40))


class Food:
    def __init__(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)
    
    def draw(self):
        pg.draw.circle(screen, GREEN, (self.x, self.y), 20)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake game")
clock = pg.time.Clock()

running = True

S1 = Snake()
F1 = Food()

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(WHITE)
    S1.draw()
    S1.move()
    F1.draw()

    pg.display.flip()
pg.quit()
