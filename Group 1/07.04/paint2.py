import pygame

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (122, 239, 173)
BROWN = (102, 51, 0)
BLACK = (0, 0, 0)
BACKGROUND = (122, 239, 173)

pygame.init()
screen = pygame.display.set_mode((800, 600))

surf = pygame.Surface((700, 600))
buttons = pygame.Surface((100, 600))

commands = {
    'line': [4, 4, 44, 44],
    'rect': [52, 4, 44, 44],
    'circle': [4,50, 44, 44],
    'eraser': [52, 50, 44, 44]
}

def set_surf():
    surf.fill(BACKGROUND)
    
    buttons.fill(WHITE)
    pygame.draw.rect(buttons, BLACK, (2, 2, 96, 596), 1)
    
    for i in commands:
        pygame.draw.rect(buttons, BLACK, commands[i], 1)
    
    pygame.draw.aaline(buttons, BLACK, (8, 8), (40, 40), 1)
    pygame.draw.rect(buttons, BLACK, (58, 10, 32, 32), 1)
    pygame.draw.circle(buttons, BLACK, (27, 70), 15, 1)

    pygame.draw.rect(buttons, BACKGROUND, (56, 58, 36, 28))
    
    
    screen.blit(surf, (0, 0))
    screen.blit(buttons, (700, 0))
    


def line(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), d)
    else:   
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), d)
        

def rectangle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1-x2)
    height = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x1, y1, width, height), d)
        else:
            pygame.draw.rect(screen, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pygame.draw.rect(screen, color, (x2, y1, width, height), d)
        else:
            pygame.draw.rect(screen, color, (x2, y2, width, height), d)



def circle(screen, start, end, d, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    width = abs(x1-x2)
    height = abs(y1-y2)

    if x1 <= x2:
        if y1 < y2:
            pygame.draw.ellipse(screen, color, (x1, y1, width, height), d)
        else:
            pygame.draw.ellipse(screen, color, (x1, y2, width, height), d)
    else:
        if y1 < y2:
            pygame.draw.ellipse(screen, color, (x2, y1, width, height), d)
        else:
            pygame.draw.ellipse(screen, color, (x2, y2, width, height), d)


last_pos = (0, 0)
w = 2
draw_line = False
erase = False
ed = 50

d = {
    'line' : True,
    'rect': False,
    'circle': False,
    'eraser': False
}

set_surf()
running = True
score = 0
while running:
    pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.image.save(surf, f'./image_{score}.jpg')
                score += 1
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for k, v in commands.items():
                if v[0] <= pos[0]-700 <= v[0] + v[2] and v[1] <= pos[1] <= v[1] + v[3]:
                    d[k] = True
                    for i, j in d.items():
                        if i != k:
                            d[i] = False
                    break
        
    
                    
        if d['line'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
                pygame.draw.circle(surf, (0, 0, 0), pos, w)
                draw_line = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_line = False
            if event.type == pygame.MOUSEMOTION:
                if draw_line:
                    line(surf, last_pos, pos, w, (0, 0, 0))
                last_pos = pos
        elif d['rect'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                rectangle(surf, last_pos, pos, w, (255, 0, 0))
        elif d['circle'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pos
            if event.type == pygame.MOUSEBUTTONUP:
                # rectangle(screen, last_pos, pos, d, (255, 0, 0))
                circle(surf, last_pos, pos, w, (255, 0, 0))
        elif d['eraser'] == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pos
                pygame.draw.rect(surf, BACKGROUND, (x, y, ed, ed))
                erase = True
            if event.type == pygame.MOUSEMOTION:
                if erase:
                    pygame.draw.rect(surf, BACKGROUND, (pos[0], pos[1], ed, ed))
            if event.type == pygame.MOUSEBUTTONUP:
                erase = False
    
    
    
    for k, v in d.items():
        if v == True:
            pygame.draw.rect(buttons, RED, commands[k], 1)
        else:
            pygame.draw.rect(buttons, BLACK, commands[k], 1)
            
    
    screen.blit(buttons, (700, 0))
    screen.blit(surf, (0, 0))
    
        

    pygame.display.update()
pygame.quit()
    
