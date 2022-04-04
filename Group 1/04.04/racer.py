import pygame as pg
import random

WIDTH = 800
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption("Hungry Lion")


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
        self.surf.blit(self.image, (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(r'./images/enemy.png')
        self.surf = pg.Surface((40, 60))
        self.rect = self.surf.get_rect(center=(random.randint(0, WIDTH - 40), -100))
        self.speed = 5
    
    def move(self):
        self.rect.move_ip(0, self.speed)
    
    def draw(self):
        self.surf.blit(self.image, (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))


class Coin(pg.sprite.Sprite):
    pass

P1 = Player()
enemies = pg.sprite.Group([Enemy() for _ in range (3)])

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(WHITE)

    P1.draw()
    P1.move()
    for enemy in enemies:
        enemy.draw()
        enemy.move()

    if pg.sprite.spritecollide(P1, enemies):
        running = False

    pg.display.update()
pg.quit()    
