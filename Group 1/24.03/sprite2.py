import pygame as pg
import random

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Surface")
clock = pg.time.Clock()

class Rectangle(pg.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.width = 70
        self.height = 30
        self.x = x
        self.y = y
        self.color = color
        self.surf = pg.Surface((self.width, self.height))
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(center=(self.x, self.y))
    
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
        
    
    def change_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.surf.fill(self.color)



class Circle(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.r = 30
        self.x = x
        self.y = y
        self.surf = pg.Surface((self.r*2, self.r*2), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
        self.draw()
    
    def move(self):
        pass

    def draw(self):
        pg.draw.circle(self.surf, (0, 0, 255), (self.r, self.r), self.r)

        

r1 = Rectangle(400, 300, RED)
c1 = Circle(random.randint(100, 700), random.randint(100, 500))
# r2 = Rectangle(600, 400, (0, 255, 0))
sprites = pg.sprite.Group([r1, c1])
enemy = pg.sprite.Group([c1])

# sprites.add(r1)
# sprites.add(c1)
# sprites.add(r2)

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = 0
    screen.fill(WHITE)
    
    for i in sprites:
        screen.blit(i.surf, i.rect)
        i.move()
    
    for i in enemy:
        screen.blit(i.surf, i.rect)



    # if pg.sprite.collide_rect(r1, c1):
    #     r1.change_color()
    #     c1.kill()
    #     sprites.add(Circle(random.randint(100, 700), random.randint(100, 500)))

    for i in enemy:
        if pg.sprite.collide_rect(r1, i):
            i.kill()
            enemy.add(Circle(random.randint(100, 700), random.randint(100, 500)))

    # if pg.sprite.spritecollideany(r1, enemy):



    pg.display.update()
pg.quit()