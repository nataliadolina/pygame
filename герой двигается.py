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


img = load_image('creature.png')
x, y = 0, 0
screen.blit(img, (x, y))
rect = img.get_rect()
running = True
screen.fill((255, 255, 255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_DOWN:
                y += 10
            elif event.key == pygame.K_UP:
                y -= 10
        screen.fill((255, 255, 255))
        screen.blit(img, (x, y))
    pygame.display.flip()
