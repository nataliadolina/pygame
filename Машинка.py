import pygame
import os

pygame.init()
x, y = 600, 95
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


class Car(pygame.sprite.Sprite):
    image = load_image("car2.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.v = 120

    def update(self, FPS):
        if self.rect.x >= 450 or self.rect.x <= -1:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.v *= -1
        self.rect = self.rect.move(int(self.v / FPS), 0)


all_sprites = pygame.sprite.Group()
fps = 60
clock = pygame.time.Clock()
Car(all_sprites)
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    all_sprites.draw(screen)
    all_sprites.update(fps)
    clock.tick(fps)
    pygame.display.flip()
