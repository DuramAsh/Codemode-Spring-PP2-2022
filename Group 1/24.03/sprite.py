from ast import While
import pygame as pg

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
        self.rect.move_ip(5, 1)
        # self.rect.x += 5
        
        if self.rect.left >= WIDTH:
            self.rect.right = 0



        

r1 = Rectangle(400, 300, RED)
r2 = Rectangle(600, 400, (0, 255, 0))
sprites = pg.sprite.Group()
sprites.add(r1)
sprites.add(r2)

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

    pg.display.update()
pg.quit()