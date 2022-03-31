# ------------------ IMPORTS ------------------
import pygame
import random
# ------------------ INITIALIZATION & VARIABLES ------------------
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
RUNNING = False
# ------------------ CLASSES ------------------


class Food:
    def __init__(self):
        self.x = random.randint(1, 20) * 40 - 20
        self.y = random.randint(1, 15) * 40 - 20

    def draw(self):
        if SPAWN:
            screen.blit(MEAT, (self.x - 18, self.y - 18))
        self.gen()

    def eaten(self, snake):
        global SPAWN
        if snake.eat(self.x, self.y):
            SPAWN = False
            self.x = random.randint(1, 20) * 40 - 20
            self.y = random.randint(1, 15) * 40 - 20
            snake.snake_grow()
            EATING_SOUND.play()

    def gen(self):
        global SPAWN
        temp_list = [self.x, self.y]
        self.eaten(S1)
        self.eaten(S2)
        if not (temp_list in S1.elements or screen.get_at((self.x - 10, self.y)) == WALL_COLOR):
            SPAWN = True
        else:
            self.x = random.randint(1, 20) * 40 - 20
            self.y = random.randint(1, 15) * 40 - 20


class Snake:
    def __init__(self, size=1, elements=[[100, 100]], dx=5, dy=0, color=(0, 0, 0), score=0):
        self.size = size
        self.color = color
        self.score = score
        self.elements = elements
        self.dx = dx
        self.dy = dy
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, self.color, (element[0] - 18, element[1] - 18, 38, 38))

    def snake_grow(self):
        global GAME_SPEED
        self.size += 1
        self.elements.append([1000, 1000])
        self.is_add = False
        if S1.size % 5 == 0:
            GAME_SPEED += 5

    def move(self):
        if self.is_add:
            self.snake_grow()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
        self.elements[0][0] %= WIDTH
        self.elements[0][1] %= HEIGHT

    def eat(self, food_x, food_y):
        if food_x == self.elements[0][0] and food_y == self.elements[0][1]:
            self.score += 1
            return True
        return False

    def collision(self):
        if self.elements[0][0] + 19 < WIDTH:
            if self.dx > 0 and (screen.get_at((self.elements[0][0] + 19, self.elements[0][1])) == WALL_COLOR or
                                screen.get_at((self.elements[0][0] + 19, self.elements[0][1])) == S1_COLOR or
                                screen.get_at((self.elements[0][0] + 19, self.elements[0][1])) == S2_COLOR):
                return True
        if self.elements[0][0] - 19 > 0:
            if self.dx < 0 and (screen.get_at((self.elements[0][0] - 19, self.elements[0][1])) == WALL_COLOR or
                                screen.get_at((self.elements[0][0] - 19, self.elements[0][1])) == S1_COLOR or
                                screen.get_at((self.elements[0][0] - 19, self.elements[0][1])) == S2_COLOR):
                return True
        if self.elements[0][1] + 19 < HEIGHT:
            if self.dy > 0 and (screen.get_at((self.elements[0][0], self.elements[0][1] + 19)) == WALL_COLOR or
                                screen.get_at((self.elements[0][0], self.elements[0][1] + 19)) == S1_COLOR or
                                screen.get_at((self.elements[0][0], self.elements[0][1] + 19)) == S2_COLOR):
                return True
        if self.elements[0][1] - 19 > 0:
            if self.dy < 0 and (screen.get_at((self.elements[0][0], self.elements[0][1] - 19)) == WALL_COLOR or
                                screen.get_at((self.elements[0][0], self.elements[0][1] - 19)) == S1_COLOR or
                                screen.get_at((self.elements[0][0], self.elements[0][1] - 19)) == S2_COLOR):
                return True


# ------------------ EXAMPLES ------------------
S1 = Snake(size=1, elements=[[100, 100]], dx=5, dy=0, color=S1_COLOR, score=0)
S2 = Snake(size=1, elements=[[700, 100]], dx=0, dy=0, color=S2_COLOR, score=0)
F1 = Food()
F2 = Food()
F3 = Food()
# ------------------ MENU LOOP ------------------
while MENU:
    with open('savefile.json', 'r') as f:
        text = json.load(f)
        d_1 = {'size': text['s1_size'], 'elements': text['s1_elements'], 'dx': text['s1_dx'], 'dy': text['s1_dy'],
               'level_index': text['level_index'], 'score': text['s1_score'], 'game_speed': text['game_speed'],
               'meat1_x': text['meat1_x'], 'meat1_y': text['meat1_y'],
               'meat2_x': text['meat2_x'], 'meat2_y': text['meat2_y'],
               'meat3_x': text['meat3_x'], 'meat3_y': text['meat3_y']}

        d_2 = {'size': text['s2_size'], 'elements': text['s2_elements'], 'dx': text['s2_dx'], 'dy': text['s2_dy'],
               'score': text['s2_score']}
        f.close()
    screen.blit(MENU_IMAGE, (0, 0))
    pygame.display.flip()
    S1 = Snake(size=1, elements=[[100, 100]], dx=5, dy=0, color=S1_COLOR, score=0)
    S2 = Snake(size=1, elements=[[700, 100]], dx=0, dy=0, color=S2_COLOR, score=0)
    GAME_SPEED = 30
    # ------------------ MENU EVENTS ------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            MENU = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                SCORE = 0
                LEVEL_INDEX = 1
                LEVEL = pygame.image.load(f'icons/level{LEVEL_INDEX}.png')
                RUNNING = True
            if keys[pygame.K_2]:
                SCORE = 0
                LEVEL_INDEX = 2
                LEVEL = pygame.image.load(f'icons/level{LEVEL_INDEX}.png')
                RUNNING = True
            if keys[pygame.K_3]:
                SCORE = 0
                LEVEL_INDEX = 3
                LEVEL = pygame.image.load(f'icons/level{LEVEL_INDEX}.png')
                RUNNING = True
            if keys[pygame.K_l]:
                LEVEL_INDEX = d_1['level_index']
                LEVEL = pygame.image.load(f'icons/level{LEVEL_INDEX}.png')
                RUNNING = True
                GAME_SPEED = d_1['game_speed']
                S1.score = d_1['score']
                S1 = Snake(d_1['size'], d_1['elements'], d_1['dx'], d_1['dy'], color=S1_COLOR, score=d_1['score'])
                S2.score = d_2['score']
                S2 = Snake(d_2['size'], d_2['elements'], d_2['dx'], d_2['dy'], color=S2_COLOR, score=d_2['score'])
                F1.x = d_1['meat1_x']
                F1.y = d_1['meat1_y']
                F2.x = d_1['meat2_x']
                F2.y = d_1['meat2_y']
                F3.x = d_1['meat3_x']
                F3.y = d_1['meat3_y']
    # ------------------ GAME LOOP ------------------
    while RUNNING:
        screen.blit(LEVEL, (0, 0))
        F1.draw()
        F2.draw()
        F3.draw()
        S1.draw()
        S2.draw()
        S1.move()
        S2.move()
        screen.blit(pygame.font.SysFont('verdana', 20).render('P1 SCORE:', True, (136, 0, 22)), (50, 40))
        screen.blit(pygame.font.SysFont('verdana', 20).render('P2 SCORE:', True, (163, 73, 165)), (625, 40))
        screen.blit(pygame.font.SysFont('verdana', 20).render(f'{S1.score}', True, (136, 0, 22)), (165, 40))
        screen.blit(pygame.font.SysFont('verdana', 20).render(f'{S2.score}', True, (163, 73, 165)), (740, 40))
        if QUICKSAVE:
            screen.blit(pygame.font.SysFont('verdana', 30).render('QUICKSAVE...', True, (0, 162, 232)), (300, 520))
        # ------------------ GAME EVENTS ------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                MENU = False
            if event.type == SAVE:
                QUICKSAVE = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] and S1.dy != 5:
                    GO_UP_S1 = True
                if keys[pygame.K_s] and S1.dy != -5:
                    GO_DOWN_S1 = True
                if keys[pygame.K_a] and S1.dx != 5:
                    GO_LEFT_S1 = True
                if keys[pygame.K_d] and S1.dx != -5:
                    GO_RIGHT_S1 = True
                if keys[pygame.K_UP] and S2.dy != 5:
                    GO_UP_S2 = True
                if keys[pygame.K_DOWN] and S2.dy != -5:
                    GO_DOWN_S2 = True
                if keys[pygame.K_LEFT] and S2.dx != 5:
                    GO_LEFT_S2 = True
                if keys[pygame.K_RIGHT] and S2.dx != -5:
                    GO_RIGHT_S2 = True
                if keys[pygame.K_ESCAPE]:
                    RUNNING = False
                    GAME_SPEED = d_1['game_speed']
                    S1 = Snake(size=1, elements=[[1000, 1000]], dx=5, dy=0, color=S1_COLOR, score=0)
                    S2 = Snake(size=1, elements=[[1000, 500]], dx=0, dy=0, color=S2_COLOR, score=0)
                    F1 = Food()
                    F2 = Food()
                    F3 = Food()
                if keys[pygame.K_F5]:
                    g = {'s1_size': S1.size, 's1_elements': S1.elements, 's1_dx': S1.dx, 's1_dy': S1.dy,
                         's1_score': S1.score,
                         's2_size': S2.size, 's2_elements': S2.elements, 's2_dx': S2.dx, 's2_dy': S2.dy,
                         's2_score': S2.score,
                         'level_index': LEVEL_INDEX, 'game_speed': GAME_SPEED,
                         'meat1_x': F1.x, 'meat1_y': F1.y,
                         'meat2_x': F2.x, 'meat2_y': F2.y,
                         'meat3_x': F3.x, 'meat3_y': F3.y}
                    with open('savefile.json', 'w') as f:
                        json.dump(g, f, indent=2)
                    f.close()
                    QUICKSAVE = True
                    pygame.time.set_timer(SAVE, 3000)
        # ------------------ COLLISION ------------------
        if S1.collision() or S2.collision():
            RUNNING = False
            GAME_SPEED = 30
            S1 = Snake(size=1, elements=[[1000, 1000]], dx=5, dy=0, color=S1_COLOR, score=0)
            S2 = Snake(size=1, elements=[[1000, 500]], dx=0, dy=0, color=S2_COLOR, score=0)
            F1 = Food()
            F2 = Food()
            F3 = Food()
        # ------------------ MOVEMENT ------------------
        if GO_UP_S1 and (S1.elements[0][0] - 20) % 40 == 0:
            S1.dx = 0
            S1.dy = -5
            GO_UP_S1 = False
        if GO_DOWN_S1 and (S1.elements[0][0] - 20) % 40 == 0:
            S1.dx = 0
            S1.dy = 5
            GO_DOWN_S1 = False
        if GO_LEFT_S1 and (S1.elements[0][1] - 20) % 40 == 0:
            S1.dx = -5
            S1.dy = 0
            GO_LEFT_S1 = False
        if GO_RIGHT_S1 and (S1.elements[0][1] - 20) % 40 == 0:
            S1.dx = 5
            S1.dy = 0
            GO_RIGHT_S1 = False
        if GO_UP_S2 and (S2.elements[0][0] - 20) % 40 == 0:
            S2.dx = 0
            S2.dy = -5
            GO_UP_S2 = False
        if GO_DOWN_S2 and (S2.elements[0][0] - 20) % 40 == 0:
            S2.dx = 0
            S2.dy = 5
            GO_DOWN_S2 = False
        if GO_LEFT_S2 and (S2.elements[0][1] - 20) % 40 == 0:
            S2.dx = -5
            S2.dy = 0
            GO_LEFT_S2 = False
        if GO_RIGHT_S2 and (S2.elements[0][1] - 20) % 40 == 0:
            S2.dx = 5
            S2.dy = 0
            GO_RIGHT_S2 = False
        # ------------------ MISC ------------------
        pygame.display.flip()
        clock.tick(GAME_SPEED)
pygame.quit()