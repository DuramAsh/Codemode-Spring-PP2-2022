from html import entities
import pygame
from random import randint
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 45

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hungry lion')

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.speed = 10
        self.surf = pygame.Surface((60,60))
        self.rect = self.surf.get_rect(center=(self.x,self.y))
    def draw(self):
        pygame.draw.rect(screen, GREEN, self.rect)
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, self.speed)

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = randint(0, WIDTH)
        self.y = HEIGHT
        self.speed = randint(3,10)
        self.surf = pygame.Surface((30,30))
        self.rect = self.surf.get_rect(center=(self.x,self.y))
    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)
    def move(self):
        self.rect.move_ip(0, -self.speed)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = randint(0, WIDTH)
        self.y = 0
        self.speed = randint(3,10)
        self.surf = pygame.Surface((30,30))
        self.rect = self.surf.get_rect(center=(self.x,self.y))
    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)
    def move(self):
        self.rect.move_ip(0, self.speed)

p = Player()

entities = pygame.sprite.Group()
foods = pygame.sprite.Group([Food() for _ in range(10)])
enemies = pygame.sprite.Group([Enemy() for _ in range(10)])

entities.add(p)
entities.add(foods)
entities.add(enemies)

score = 0
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            restart = False
            finished = True
    screen.fill(BLACK)

    for entity in entities:
        entity.draw()
        entity.move()

    for food in foods:
        if pygame.sprite.collide_rect(p, food):
            food.kill()
            score += 1
            newFood = Food()
            foods.add(newFood)
            entities.add(newFood)
    
    for enemy in enemies:
        if pygame.sprite.collide_rect(p, enemy):
            enemy.kill()
            score -= 1
            newEnemy = Enemy()
            enemies.add(newEnemy)
            entities.add(newEnemy)
        
    pygame.display.flip()
pygame.quit()