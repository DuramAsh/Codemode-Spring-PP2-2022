from cmath import rect
from turtle import speed
import pygame
pygame.init()
pygame.display.set_caption("AIBERGENOID")

WIDTH = 800
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self surf
        self rect
        self speed
        
    def draw
    
    def move


class Ball(pygame.sprite.Sprite):
    def __init(self):
        super().__init__()
        self surf
        self rect
        self speed
        self radius
        self color # Optional
        
        
r1 = pygame.Rect()
    def draw
    
    def move


class Brick(pygame.sprite.Sprite):
    def __init(self):
        super().__init__()
        self surf
        self rect
        self color  # Optional
    
    def draw


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.display.flip()
pygame.quit()
