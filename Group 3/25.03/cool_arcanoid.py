import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 45

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('"OOP" Arcanoid')

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)


restart = True

ZHANTORE = pygame.image.load("./img/zhantore.png")

area = (700, 300)
each = (33, 18)

def find_pos():
    positions = []
    for i in range(50, area[0] + 50, 35):
            for j in range(50, area[1] + 50, 20):
                # pygame.draw.rect(screen, BLACK, (i, j, each[0], each[1]))
                positions.append((i, j))
    return positions

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, rad, color = RED):
        super().__init__()
        self.x, self.y = x, y
        self.rad = rad
        self.color = color
        self.dx, self.dy = -3, -3
        self.surf = pygame.Surface((self.rad * 2, self.rad * 2), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))

    def draw(self):
        self.surf.blit(ZHANTORE, (0,0))
        screen.blit(self.surf, self.rect) # ! ALINA ! -> self.rect
        
    def move(self):
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.dx *= -1
        if self.rect.top <= 0:
            self.dy *= -1

        self.rect.move_ip(self.dx, self.dy)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, step, width, height, color):
        super().__init__()
        self.x, self.y = x, y
        self.color = color
        self.step = step
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-self.step, 0)
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(self.step, 0)



class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.x, self.y = x, y
        self.color = color
        self.surf = pygame.Surface((each[0], each[1]))
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    def draw(self):
        pygame.draw.rect(self.surf, self.color, self.rect)
        screen.blit(self.surf, self.rect)





while restart:
    finished = False
    lose = False
    win = False
    ball = Ball(WIDTH // 2, HEIGHT // 2 + 100, 15)
    player = Player(WIDTH // 2, 500, 10, 200, 30, BLUE)

    entities = pygame.sprite.Group()
    brickz = pygame.sprite.Group()

    for x, y in find_pos():
        brickz.add(Brick(x, y, GREEN))

    entities.add(player)
    entities.add(ball)

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = False
                finished = True
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            #     lose = True

        screen.fill(PURPLE)

        for each in entities:
            each.draw()
            each.move()

        for each in brickz:
            each.draw()

        

       
        if pygame.sprite.collide_rect(ball, player):
            ball.dy *= -1 
        
        


        while lose or win:
            pygame.draw.rect(screen, WHITE, (150, 100, 500, 400))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    restart = False
                    finished = True
                    lose = False
                    win = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    lose = False
                    win = False
                    finished = True


            pygame.display.flip()
        pygame.display.flip()
    pygame.display.flip()
pygame.quit()