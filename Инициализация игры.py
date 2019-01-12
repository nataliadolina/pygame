import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 [self.top + self.cell_size * j, self.left + self.cell_size*i, self.cell_size,
                                  self.cell_size], 1)


pygame.init()
x, y = 800, 800
size = width, height = x, y
screen = pygame.display.set_mode(size)
while pygame.event.wait().type != pygame.QUIT:
    pass
    pygame.display.flip()
