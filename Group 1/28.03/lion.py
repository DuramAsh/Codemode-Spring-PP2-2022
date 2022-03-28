import pygame as pg
from random import *

WIDTH = 800
HEIGHT = 600
FPS = 60
BLACK = (0, 0, 0)
WHITE = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
pg.display.set_caption("Hungry Lion")
bg = pg.image.load("background.jpg")
pg.mixer.music.load('Ric Flair Scrip.mp3')
pg.mixer.music.play(-1)


class Hero(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 20
        self.height = 20
        self.x = x
        self.y = y
        self.surf = pg.Surface((self.x, self.y))
        self.rect = self.surf.get_rect(center=(self.x, self.y))
        self.image = pg.image.load("roocket.png")
    
    def move(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT]:
            if self.rect.right <= 0:
                self.rect.left = WIDTH
            self.rect.move_ip(-5, 0)

        if keys[pg.K_RIGHT]:
            if self.rect.left >= WIDTH:
                self.rect.right = 0
            self.rect.move_ip(5, 0)

        if keys[pg.K_DOWN]:
            if self.rect.top >= HEIGHT:
                self.rect.bottom = 0
            self.rect.move_ip(0, 5)

        if keys[pg.K_UP]:
            if self.rect.bottom <= 0:
                self.rect.top = HEIGHT
            self.rect.move_ip(0, -5)
    def draw(self):
        screen.blit(self.image, self.rect)


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pg.image.load("ico256.png")
        self.x = randint(0, WIDTH)
        self.y = randint(0, 300) * -1
        # self.y = 0
        self.speed = 2
        self.surf = pg.Surface((20, 20))
        self.rect = self.surf.get_rect(center=(self.x, self.y))
    
    def move(self):
        if self.rect.bottom >= HEIGHT:
            self.rect = self.surf.get_rect(center=(randint(0, WIDTH), 0)) 
        self.rect.move_ip(0, self.speed)

    def draw(self):
        screen.blit(self.img, self.rect)


class Eda(pg.sprite.Sprite): 
    def __init__(self, x, y): 
        super().__init__() 
        self.im = pg.image.load('pic1.png') 
        self.x = x 
        self.y = y 
        self.surf = pg.Surface((20, 20), pg.SRCALPHA) 
        self.rect = self.surf.get_rect(center=(self.x, self.y)) 

    def draw(self): 
        self.surf.blit(self.im, (0, 0))
        screen.blit(self.surf, self.rect) 
        

    def move(self): 
        if self.rect.top <= 0:
            self.rect = self.surf.get_rect(center=(randint(0, WIDTH), HEIGHT)) 

        self.rect.move_ip(0, -2) 



player = Hero(WIDTH // 2, HEIGHT // 2 + 300)
foods = [Eda(randint(0, WIDTH), randint(HEIGHT, HEIGHT * 2)) for i in range(20)]
# foods = [Eda(randint(0, WIDTH), HEIGHT) for i in range(20)]
enemies = [Enemy() for i in range(10)]


all_sprites = pg.sprite.Group([player] + foods + enemies)
food_sprites = pg.sprite.Group(foods)
enemy_sprites = pg.sprite.Group(enemies)



running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(bg, (0, 0))

    for i in all_sprites:
        i.draw()
        i.move()
    

    pg.display.flip()
pg.quit()
        
