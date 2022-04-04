import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))


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


last_pos = (0, 0)
d = 2
draw_line = False

running = True
while running:
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            last_pos = pos
        if event.type == pygame.MOUSEBUTTONUP:
            rectangle(screen, last_pos, pos, d, (255, 0, 0))
        
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     last_pos = pos
            #     pygame.draw.circle(screen, (0, 0, 0), pos, d)
            #     draw_line = True
            # if event.type == pygame.MOUSEBUTTONUP:
            #     draw_line = False
            # if event.type == pygame.MOUSEMOTION:
            #     if draw_line:
            #         line(screen, last_pos, pos, d, (0, 0, 0))
            #     last_pos = pos
        # elif event.key == pygame.K_r:
        

    pygame.display.update()
pygame.quit()
    
