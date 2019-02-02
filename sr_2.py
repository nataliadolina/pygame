import pygame
import os

pygame.init()
x, y = 101, 600
size = width, height = x, y
running = True
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))


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


class Sprite_1(pygame.sprite.Sprite):
    image = load_image("sprite.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Sprite_1.image
        self.rect = self.image.get_rect()
        self.v = 0
        self.arr = []

    def update(self, FPS):
        self.rect = self.rect.move(int(self.v / FPS), 0)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            self.v = 50


all_sprites = pygame.sprite.Group()
fps = 25
clock = pygame.time.Clock()
k = 0
arr = []
for i in range(3):
    Sprite_1(all_sprites)
for i in all_sprites:
    i.rect.y = 200 * k
    k += 1
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            for i in all_sprites:
                i.get_event(event)
    all_sprites.draw(screen)
    all_sprites.update(fps)
    clock.tick(fps)
    pygame.display.flip()
