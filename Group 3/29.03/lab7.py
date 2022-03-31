import pygame, datetime
pygame.init()

WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

FPS = 60


def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)

def blitRotate2(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)



finished = False
current = datetime.datetime.now()
seconds = current.second
minute = current.minute

while not finished:
    
    clock.tick(FPS)

    angle = (360 / 60) * seconds
    angle_2 = (360 / 60) * (minute + seconds / 60)
    # blitRotate(screen, image, (WIDTH // 2, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2), )
    # 15 minutes = 60 * 15 = 900

