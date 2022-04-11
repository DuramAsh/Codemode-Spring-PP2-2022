import pygame
from constants import *
from random import randint
import math
pygame.init()

background = pygame.transform.scale(pygame.image.load(r".\images\bg.jpeg"), (WIDTH, HEIGHT))
bgY = 0
bgY2 = - background.get_height()
BGSPEED = 7

shock_sound = pygame.mixer.Sound("bob.mp3")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hungry lion')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 400
        self.y = 500
        self.speed = 10
        self.image = pygame.transform.scale(pygame.image.load('.\images\Audi.png'),(40,90))
        self.surf = pygame.Surface((40, 90), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center=(self.x,self.y))
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_RIGHT] and self.rect.right <= WIDTH:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_UP] and self.rect.top >= 0:
            self.rect.move_ip(0,-self.speed)
        if keys[pygame.K_DOWN] and self.rect.bottom <= HEIGHT:
            self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(self.image, (0, 0))
        screen.blit(self.surf, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = randint(10, 15)
        self.x = randint(80, WIDTH - 80)
        self.y = -100
        self.image = pygame.transform.scale(pygame.image.load(".\images\Police.png"), (40,90))
        self.surf = pygame.Surface((40,90), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    
    def move(self):
        self.rect.move_ip(0, self.speed)
    
    def draw(self):
        self.surf.blit(self.image, (0,0))
        screen.blit(self.surf, self.rect)

    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = randint(10, 15)
        self.x = randint(80, WIDTH - 80)
        self.y = -100
        self.image = pygame.transform.scale(pygame.image.load(".\images\Gold_1.png"), (25,25))
        self.surf = pygame.Surface((25,25), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))

        self.images = [pygame.image.load(f"./coin_images/c{i}.png") for i in range(1, 7)]
        self.anim_cnt = 0
    
    def move(self):
        self.rect.move_ip(0, self.speed)
        
    
    def draw(self):
        self.surf.blit(self.image, (0,0))
        screen.blit(self.surf, self.rect)
    
    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()

    def animate(self):
        self.anim_cnt += 1
        self.image = self.images[self.anim_cnt % len(self.images)]


clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 25)
font_large = pygame.font.SysFont("Times New Roman", 75)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)

enemies = pygame.sprite.Group([Enemy() for _ in range(5)])
coins = pygame.sprite.Group([Coin() for _ in range(7)])
p = Player()

SHOCK = pygame.USEREVENT

FAST = pygame.USEREVENT + 1
NOT_FAST = pygame.USEREVENT + 2
FLIP = pygame.USEREVENT + 3

# pygame.time.set_timer(SHOCK, 5000)
pygame.time.set_timer(FLIP, 100)


SCORE = 0
game_over = font_large.render("GAME OVER", False, BLACK)
finished = False
lose = False


car_images = [pygame.transform.rotate(p.image, math.radians(i)) for i in range(361)]
flame = pygame.image.load('./images/flame.png')
flame = pygame.transform.scale(flame, (100, 100))
flame = pygame.transform.rotate(flame, 180)

animation_count = 0
car_animation_count = 0

while not finished:
    clock.tick(FPS)
    

    if car_animation_count + 1 > 360:
        animation_count = 0 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        
        if event.type == SHOCK:
            shock_sound.play()

        # if event.type == FAST:
        #     FPS = 50
        # if event.type == NOT_FAST:
        #     FPS = 30
        if event.type == FLIP:
            for coin in coins:
                coin.animate()
        
        


    screen.blit(background,(0,bgY))
    screen.blit(background,(0,bgY2))

    if bgY > background.get_height():
        bgY = -background.get_height()
    if bgY2 > background.get_height():
        bgY2 = -background.get_height()
    bgY += BGSPEED
    bgY2 += BGSPEED

    text = font.render(f"SCORE: {SCORE}", False, RED)
    screen.blit(text, (50,20))

    p.image = car_images[animation_count]
    p.draw()
    p.move()
    
    if len(enemies) < 5:
        enemies.add(Enemy())
    if len(coins) < 7:
        coins.add(Coin())
    
    if SCORE % 5 == 0:
        pygame.time.set_timer(FAST, 50, loops = False)
        pygame.time.set_timer(NOT_FAST, 150, loops = False)
        

    # for enemy in enemies:
    #     enemy.draw()
    #     enemy.move()
    #     enemy.kil()

    screen.blit(flame, (p.rect.bottomleft[0] - 20, p.rect.bottomleft[1] ))

    for coin in coins:
        coin.draw()
        coin.move()
        coin.kil()

    if pygame.sprite.spritecollide(p, enemies, False):
        lose = True

    for coin in coins:
        if pygame.sprite.collide_rect(p, coin):
            coin.kill()
            SCORE += 1
            coins.add(Coin())

    for enemy in enemies:
        for enemy2 in enemies:
            if enemy != enemy2 and pygame.sprite.collide_rect(enemy, enemy2):
                enemy2.kill()
    
    while lose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                lose = False
        pygame.draw.rect(screen, WHITE, (100, 75, 600, 400))
        screen.blit(game_over, (100,100))
        pygame.display.flip()

    pygame.display.flip()
pygame.quit()