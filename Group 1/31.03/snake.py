import pygame as pg
from random import randint

WIDTH = 800
HEIGHT = 600
FPS = 30
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
        self.body = [[80, 80]]
        self.dx = 10
        self.dy = 0
        self.is_add = False

    def grow(self):
        self.length += 1
        self.is_add = False
        self.body.append([1000, 1000])

    def move(self):
        if self.is_add:
            self.add_to_snake()

        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            if self.body[0][1] % 40 == 0:
                self.dx = -10
                self.dy = 0
        if keys[pg.K_d]:
            if self.body[0][1] % 40 == 0:
                self.dx = 10
                self.dy = 0
        if keys[pg.K_w]:
            if self.body[0][0] % 40 == 0:
                self.dy = -10
                self.dx = 0
        if keys[pg.K_s]:
            if self.body[0][0] % 40 == 0:
                self.dy = 10
                self.dx = 0

        for part in range(self.length - 1, 0, -1):
            self.body[part][0] = self.body[part - 1][0]
            self.body[part][1] = self.body[part - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

    def draw(self):
        for part in self.body:
            pg.draw.rect(screen, self.color, (part[0], part[1], 40, 40))

    def eat(self, food_x, food_y):
        x = self.body[0][0]
        y = self.body[0][1]

        if x == food_x + 20 and y == food_y + 20:
            return True
        return False


class Food:
    def __init__(self):
        self.x = randint(0, WIDTH) % 20 * 40
        self.y = randint(0, HEIGHT) % 20 * 40
        self.r = 20

    def draw(self):
        pg.draw.circle(
            screen, GREEN, (self.x + self.r, self.y + self.r), self.r)

    def gen(self):
        self.x = randint(0, WIDTH) % 20 * 40
        self.y = randint(0, HEIGHT) % 20 * 40

    


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
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                S1.grow() 

    if F1.eaten(S1):
        print("done")
        S1.is_add = True
        F1.gen()

    screen.fill(WHITE)
    S1.draw()
    S1.move()
    F1.draw()

    pg.display.flip()
pg.quit()
