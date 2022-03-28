import pygame as pg

# add score
# add collisions with PLayer, with walls
# add game over
# EXTRA:
# make bricks going down 
# change direction of ball depending on collision side

WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

LOCATIONS = {
    30:  [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720],
    70: [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720],
    110: [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720]
}

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Surface")
clock = pg.time.Clock()

running = True


class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.surf = pg.Surface((400, 20))
        self.rect = self.surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))
        self.color = GREEN

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            pass

    def draw(self):
        self.surf.fill(self.color)
        screen.blit(self.surf, self.rect)


class Ball(pg.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.r = 20
        self.x = x
        self.y = y
        self.color = RED
        self.surf = pg.Surface((40, 40), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(self.x, self.y))
        self.dx = 5
        self.dy = -5

    def move(self):
        self.rect.move_ip(self.dx, self.dy)

    def draw(self):
        pg.draw.circle(self.surf, self.color, (self.r, self.r), self.r)
        screen.blit(self.surf, self.rect)


class Brick(pg.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.surf = pg.Surface((40, 30))
        self.rect = self.surf.get_rect(center=(self.x, self.y))
    
    def draw(self):
        screen.blit(self.surf, self.rect)


P1 = Player()
B1 = Ball(WIDTH // 2, HEIGHT // 2 + 100)
entities = pg.sprite.Group([P1, B1])
enemies = pg.sprite.Group()
for y, i in LOCATIONS.items():
    for j in i:
        enemies.add(Brick(j, y)) 

while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(WHITE)

    for entity in entities:
        entity.draw()
        entity.move()
    
    for enemy in enemies:
        enemy.draw()
        if pg.sprite.collide_rect(B1, enemy):
            enemy.kill()
            # change direction of ball

    

    pg.display.flip()
pg.quit()
