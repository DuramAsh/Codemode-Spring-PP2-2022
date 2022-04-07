import pygame as pg
import random
import json

WIDTH = 800
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
score = 0
d = {}
d['highscore'] = -1
y = 0
ry = 2

MEGA_COIN = pg.USEREVENT + 1
FREEZE = pg.USEREVENT + 2
FLIP = pg.USEREVENT + 3

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption("Nura v Aktobe")

font = pg.font.SysFont('Times New Roman', 40)
pg.time.set_timer(FLIP, 150)

road = pg.image.load('./images/road.png')

try:
    with open('save.json', 'r') as f:
        d = json.loads(f.read())
except Exception as e:
    print(str(e))


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r'./images/player.jpg')
        self.surf = pg.Surface((40, 60))
        self.rect = self.surf.get_rect(center=(400, 500))
        self.speed = 5

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_i] and self.rect.top > 0:
            self.rect.move_ip(0, -self.speed)
        if keys[pg.K_k] and self.rect.bottom < HEIGHT:
            self.rect.move_ip(0, self.speed)
        if keys[pg.K_j] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pg.K_l] and self.rect.right < WIDTH:
            self.rect.move_ip(self.speed, 0)

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (40, 60)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r'./images/enemy.png')
        self.surf = pg.Surface((40, 60))
        self.rect = self.surf.get_rect(
            center=(random.randint(0, WIDTH - 40), -100))
        self.speed = random.randint(3, 5)

    def move(self):
        self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (40, 60)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def ubivat(self):
        if self.rect.top > HEIGHT:
            self.kill()


class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pg.Surface((20, 20))
        self.rect = self.surf.get_rect(
            center=(random.randint(0, WIDTH - 40), -100))
        self.speed = random.randint(1, 8)
        self.animation_index = 0
        self.random_number = random.randint(0, 9)
        self.images = [
            './coin_images/c1.png',
            './coin_images/c2.png',
            './coin_images/c3.png',
            './coin_images/c4.png',
            './coin_images/c5.png',
            './coin_images/c6.png'
        ]
        self.image = pg.image.load(self.images[0])
        self.mega_coin()

    def move(self):
        self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(pg.transform.scale(self.image, (20, 20)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def animate(self):
        self.animation_index += 1
        if self.animation_index >= len(self.images):
            self.animation_index = 0
        self.image = pg.image.load(self.images[self.animation_index])

    def ubivat(self):
        if self.rect.top > HEIGHT:
            self.kill()

    def mega_coin(self):
        if self.random_number in [0, 1, 2]:
            self.image = pg.image.load(self.images[1])
            # self.speed = 15
        else:
            self.image = pg.image.load(self.images[0])

    def is_mega_coin(self):
        return self.random_number == 10


P1 = Player()
enemies = pg.sprite.Group([Enemy() for _ in range(3)])
coins = pg.sprite.Group([Coin() for _ in range(5)])

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # if event.type == MEGA_COIN:
        #     P1.speed = 30
        if event.type == FLIP:
            for coin in coins:
                coin.animate()

    screen.fill(WHITE)
    screen.blit(pg.transform.scale(road, (WIDTH, HEIGHT)), (0, y % HEIGHT))
    screen.blit(pg.transform.scale(road, (WIDTH, HEIGHT)), (0, -HEIGHT + (y % HEIGHT)))

    y += ry

    P1.draw()
    P1.move()
    for enemy in enemies:
        enemy.draw()
        enemy.move()
        enemy.ubivat()

    for coin in coins:
        coin.draw()
        coin.move()
        # coin.animate()
        coin.ubivat()

    if enemies.__len__() < 3:
        enemies.add(Enemy())

    if coins.__len__() < 5:
        coins.add(Coin())

    if pg.sprite.spritecollide(P1, enemies, False):
        running = False
        with open('save.json', 'w') as f:
            f.write(json.dumps(d, indent=4))

    for coin in pg.sprite.spritecollide(P1, coins, True):
        score += 1
        if coin.is_mega_coin():
            score += 100
            pg.time.set_timer(MEGA_COIN, 5000, loops=False)

    if score > d['highscore']:
        d['highscore'] = score

    text = font.render(f"{score}", True, BLACK)
    screen.blit(text, (20, 20))

    pg.display.update()
pg.quit()
