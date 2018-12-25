import pygame

pygame.init()
s = map(int, input().split())
s, n = s
w = s // n
size = width, height = s, s
screen = pygame.display.set_mode(size)
for i in range(n):
    for j in range(n):
        if n % 2 == 1:
            if (j + i) % 2 == 0:
                pygame.draw.rect(screen, (0, 0, 0), [i * w, j * w, w, w])
            else:
                pygame.draw.rect(screen, (255, 255, 255), [i * w, j * w, w, w])
        else:
            if (j + i) % 2 == 1:
                pygame.draw.rect(screen, (0, 0, 0), [i * w, j * w, w, w])
            else:
                pygame.draw.rect(screen, (255, 255, 255), [i * w, j * w, w, w])
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
