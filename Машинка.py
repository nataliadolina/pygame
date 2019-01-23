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

    def update(self, x1):
        self.rect = self.rect.move(x1, 0)

    def check_coords(self):
        pygame.transform.flip(self.image, 1, 0)


all_sprites = pygame.sprite.Group()
fps = 60
v = 1
clock = pygame.time.Clock()
Car(all_sprites)
x = 0
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    for i in all_sprites:
        if i.rect.x == 600:
            i.check_coords()
            v = -v
    all_sprites.draw(screen)
    x += v / fps
    all_sprites.update(x)
    clock.tick(fps)
    pygame.display.flip()
