import pygame
import os
from random import randrange

pygame.init()
x, y = 500, 500
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


class Bomb:
    def __init__(self, k):
        self.k = k

    def show_bomb(self):
        for i in range(self.k):
            x1, y1 = randrange(1, 501), randrange(1, 501)
            sprite = pygame.sprite.Sprite()
            sprite.image = load_image("bomb.png")
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = x1
            sprite.rect.y = y1
            all_sprites.add(sprite)
        all_sprites.draw(screen)


boom = load_image('boom.png')
x, y = 0, 0
running = True
screen.fill((255, 255, 255))
all_sprites = pygame.sprite.Group()
ex = Bomb(20)
ex.show_bomb()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            for i in all_sprites:
                rect = i.rect
                if rect.collidepoint(pos):
                    i.image = load_image('boom.png')

    pygame.display.flip()
