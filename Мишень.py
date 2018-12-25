import pygame

pygame.init()
n = int(input())
k = int(input())
a = n * k * 6
size = width, height = a, a
screen = pygame.display.set_mode(size)
pos = a // 2
radius = a // 2
while radius > 0:
    if radius > 0:
        pygame.draw.circle(screen, (0, 0, 255), [pos, pos], radius)
        radius -= n
    if radius > 0:
        pygame.draw.circle(screen, (0, 255, 0), [pos, pos], radius)
        radius -= n
    if radius > 0:
        pygame.draw.circle(screen, (255, 0, 0), [pos, pos], radius)
        radius -= n
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
