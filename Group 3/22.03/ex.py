import pygame, random
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((40, 40))
        self.rect = self.surf.get_rect(center=(400, 500))
        self.speed = 3

    def draw(self):
        pygame.draw.circle(screen, (0, 0, 0),
                           (self.rect.x + 20, self.rect.y + 20), 20)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_d]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_w]:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_s]:
            self.rect.move_ip(0, self.speed)


class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((40, 20))
        self.rect = self.surf.get_rect(center=(random.randint(100, 700), 100))
    
    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.rect.x, self.rect.y, 40, 20))
    


B1 = Ball()
Br1 = Brick()
Br2 = Brick()

ballz = pygame.sprite.Group()
ballz.add(B1)

bricks = pygame.sprite.Group()
bricks.add(Br1)
bricks.add(Br2)

entities = pygame.sprite.Group()
entities.add(B1)
entities.add(Br1)
entities.add(Br2)
clock = pygame.time.Clock()
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    for entity in entities:
        entity.draw()
    for ball in ballz:
        ball.move()

    if pygame.sprite.spritecollide(B1, bricks, True):
        print('KILLED')

    # print(B1.rect.x, B1.rect.y)
    # pygame.draw.line(screen, (0, 0, 0), (380, 480), (380, 480), 1)

    pygame.display.flip()
pygame.quit()
