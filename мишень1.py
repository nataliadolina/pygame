import pygame

pygame.init()
n = int(input())
k = int(input())
a = n * k * 2
size = width, height = a, a
screen = pygame.display.set_mode(size)
pos = a // 2
radius = a // 2
color = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]
n1 = 0
for i in range(radius, -1, -n):
    if i != 0:
        pygame.draw.circle(screen, color[n1 % 3], [pos, pos], i)
    n1 += 1
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
