import pygame, psycopg2
from config import data
from random import randint, randrange

username = input()

config = psycopg2.connect(**data)

current = config.cursor()



sql = '''
    SELECT * FROM users WHERE user_name = %s;
'''
current.execute(sql,(username,))

output = current.fetchone()

if output == None:
    sql = '''
        INSERT INTO users VALUES(%s);
    '''
    current.execute(sql,(username,))
    config.commit()

# else:
#     sql = f'''
#         SELECT level FROM users WHERE user_name = %s;
#     '''

#     current.execute(sql,(username,))

#     lvl_from_db = current.fetchone()
#     print(lvl_from_db)




pygame.init()

WIDTH, HEIGHT = 800, 800
FPS = 10
cell = 40


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (221,160,221)
SCORE = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

finished = False

clock = pygame.time.Clock()

class Food:
    def __init__(self):
        # self.x = randint(0, WIDTH) % cell * 40
        # self.y = randint(0, HEIGHT) % cell * 40
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, cell, cell)) 
    def redraw(self):
        self.x = randrange(0, WIDTH, cell)
        self.y = randrange(0, HEIGHT, cell)

class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, cell, cell))

class Snake:
    def __init__(self):
        self.speed = cell
        self.body = [[80, 80],[1000,1000],[1040,1040],[1080,1080],[1120,1120]]
        self.dx = self.speed
        self.dy = 0
        self.destination = ''
        self.color = GREEN
    
    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.destination != 'right':
                    self.dx = -self.speed
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_d and self.destination != 'left':
                    self.dx = self.speed
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_w and self.destination != 'down':
                    self.dx = 0
                    self.dy = -self.speed
                    self.destination = 'up'
                if event.key == pygame.K_s and self.destination != 'up':
                    self.dx = 0
                    self.dy = self.speed
                    self.destination = 'down'
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        self.body[0][0] %= WIDTH
        self.body[0][1] %= HEIGHT


    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, self.color, (block[0], block[1], cell, cell))
    
    def collide_food(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            # f.redraw()
            self.body.append([1000, 1000])
    
    def collide_self(self):
        global finished
        if self.body[0] in self.body[1:]:
            finished = True

    def check_food(self, f:Food):
        if [f.x, f.y] in self.body:
            f.redraw()

    
    


s = Snake()
f = Food()



level = 0

while not finished:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            level += 1
            level %= 2
        
    screen.fill(WHITE)



    for i in range(0, WIDTH, cell):
        for j in range(0, HEIGHT, cell):
            pygame.draw.rect(screen, BLACK, (i, j, cell, cell), 1)

    
    walls_coor = open(f'wall{level}.txt', 'r').readlines()
    # C:\Users\Бауыржан\Documents\Codemode-Spring-PP2-2022\Group 3\01.04\snake.py


    walls = []

    for i, line in enumerate(walls_coor):
        for j, each in enumerate(line):
            if each == "#":
                walls.append(Wall(j * cell, i * cell))

    
    SCORE = len(s.body)
    f.draw()
    s.draw()
    s.move(events)
    s.collide_food(f)
    s.collide_self()
    s.check_food(f)

    for wall in walls:
        wall.draw()
        if f.x == wall.x and f.y == wall.y:
            f.redraw()

        if s.body[0][0] == wall.x and s.body[0][1] == wall.y:
            finished = True

    pygame.display.flip()



# if finished:
#     sql = '''
#         SELECT score FROM users WHERE user_name = %s;
#     '''
#     current.execute(sql,(username,))
#     score_from_db = current.fetchone()
#     if SCORE > int(score_from_db[0]):
#         sql = '''
#             UPDATE users SET score=%s, level=%s WHERE user_name=%s;
#         '''
#         current.execute(sql,(SCORE,level,username))
#         config.commit()

# current.close()
# config.commit()
# config.close()
pygame.quit()