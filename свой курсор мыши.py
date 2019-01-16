import pygame
import os

pygame.init()
x, y = 300, 300
size = width, height = x, y
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


img = load_image('arrow.png')
running = True
pygame.mouse.set_visible(False)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            screen.fill((0, 0, 0))
            if pygame.mouse.get_focused():
                screen.blit(img, pos)
    pygame.display.flip()
