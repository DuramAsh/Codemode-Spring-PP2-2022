import pygame
import random
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 30


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((60, 60))
        self.speed = 3
        self.radius = 30
        self.rect = self.surf.get_rect(center=((WIDTH // 2, HEIGHT // 2)))

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

    def draw(self):
        # self.surf.fill(RED)
        # screen.blit(self.surf, (self.rect.x, self.rect.y))
        pygame.draw.circle(
            screen, WHITE, (self.rect.x + self.radius, self.rect.y + self.radius), self.radius)


class Brick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 25))
        self.rect = self.surf.get_rect(
            topleft=(random.randint(0, WIDTH - 50), 100))

    def draw(self):
        pygame.draw.rect(screen, RED, (self.rect.x, self.rect.y, 50, 25))
        # self.surf.fill(BLUE)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

run = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


B1 = Ball()
SCORE = 0
entities = pygame.sprite.Group()
ballz = pygame.sprite.Group()
brickz = pygame.sprite.Group([Brick() for _ in range(5)])

# entities.add(Br1)
# entities.add(Br2)
# entities.add(Br3)
entities.add(B1)

ballz.add(B1)

# brickz.add(Br1)
# brickz.add(Br2)
# brickz.add(Br3)

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(BLACK)

    # for entity in entities:
    #     entity.draw()
    for brick in brickz:
        brick.draw()
    for ball in ballz:
        ball.draw()
        ball.move()

    if pygame.sprite.spritecollide(B1, brickz, True):
        SCORE += 1
        print(SCORE)

    pygame.display.flip()
pygame.quit()
