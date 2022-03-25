import pygame as pg
import random
import json

pg.init()
pg.mixer.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ZHANTORE = pg.image.load("zhantore.png")
FONT = pg.font.SysFont("Times New Roman", 20, True)
SCORE = 0
HIGHSCORE = 0
DICT = {}

LOCATIONS = {
    30:  [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720],
    70: [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720],
    110: [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720]
}

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Arcanoid")
clock = pg.time.Clock()


class Line(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.width = 300
        self.height = 30
        self.x = 250
        self.y = 500
        self.surf = pg.Surface((self.width, self.height))
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect(center=(self.x, self.y))

    def move(self):
        # global WIDTH
        keys = pg.key.get_pressed()

        if self.rect.left > 0:
            if keys[pg.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:
            if keys[pg.K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self):
        screen.blit(self.surf, self.rect)


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.r = 15
        self.x = random.randint(20, 770)
        self.y = random.randint(400, 500)
        self.dx = 4
        self.dy = -4
        self.angle = 0
        self.init_ball()

    def init_ball(self):
        self.surf = pg.Surface((self.r * 2, self.r * 2), pg.SRCALPHA)

        self.rect = self.surf.get_rect(center=(self.x, self.y))
        # pg.draw.circle(self.surf, RED, (self.r, self.r), self.r)
        self.surf.blit(ZHANTORE, (0, 0))

    def move(self):
        global WIDTH, HEIGHT
        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.dx *= -1
        if self.rect.top <= 0:
            self.dy *= -1

        self.x += self.dx
        self.y += self.dy
        self.init_ball()

    def draw(self):
        self.angle += 1
        self.surf = pg.transform.rotate(self.surf, self.angle % 360)
        screen.blit(self.surf, self.rect)


class Enemy(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.surf = pg.Surface((40, 30))
        self.rect = self.surf.get_rect(center=(self.x, self.y))


line = Line()
ball = Ball()

sprites = pg.sprite.Group()
enemies = pg.sprite.Group()

sprites.add(line)
sprites.add(ball)

for y, i in LOCATIONS.items():
    for j in i:
        enemies.add(Enemy(j, y))

running = True
while running:
    with open("savefile.json", "r") as f:
        DICT = json.loads(f.read())
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # with open("savefile.json", "r") as f:
            #     global d
            #     d = json.loads(f.read())
            # with open("savefile.json", "w") as f:
            #     if SCORE > d['highscore']:
            #         d['highscore'] = SCORE
            #     l = json.dumps(d, indent=4)
            #     f.write(l)
            running = False
    screen.fill(WHITE)

    for i in sprites:
        i.draw()
        i.move()

    for i in enemies:
        screen.blit(i.surf, i.rect)

    if pg.sprite.collide_rect(line, ball):
        ball.dy *= -1
        # pg.mixer.Sound("ya.mp3").play()

    for e in enemies:
        # if pg.sprite.collide_rect(ball, e):
        if e.rect.bottom == ball.rect.top or e.rect.top == ball.rect.bottom:
            ball.dy *= -1
            e.kill()
            SCORE += 1
            pg.mixer.Sound("ya.mp3").play()
            with open("savefile.json", "w") as f:
                if SCORE > DICT['highscore']:
                    DICT['highscore'] = SCORE
                l = json.dumps(DICT, indent=4)
                f.write(l)
        elif e.rect.left == ball.rect.right or e.rect.right == ball.rect.left:
            ball.dx *= -1
            e.kill()
            SCORE += 1
            pg.mixer.Sound("ya.mp3").play()
            with open("savefile.json", "w") as f:
                if SCORE > DICT['highscore']:
                    DICT['highscore'] = SCORE
                l = json.dumps(DICT, indent=4)
                f.write(l)

    screen.blit(FONT.render(f"Score: {SCORE}", False, False), (0, 250))
    screen.blit(FONT.render(
        f"Highscore: {DICT['highscore']}", False, False), (0, 150))

    pg.display.update()
pg.quit()
