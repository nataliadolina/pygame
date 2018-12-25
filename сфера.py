import pygame

pygame.init()
n = int(input())
h = 300
a = 300 // (n * 2)
f = 0
size = width, height = h, h
screen = pygame.display.set_mode(size)
for i in range(n):
    if h > 0:
        pygame.draw.ellipse(screen, (255, 255, 255), [f, 0, h - f, 300], 1)
        pygame.draw.ellipse(screen, (255, 255, 255), [0, f, 300, h - f], 1)
        h -= a
        f += a
    else:
        break
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
