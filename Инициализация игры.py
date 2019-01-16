import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.coords = []

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 [self.top + self.cell_size * j, self.left + self.cell_size * i, self.cell_size,
                                  self.cell_size], 1)
                self.coords.append((j, i))


pygame.init()
x, y = 300, 300
size = width, height = x, y
screen = pygame.display.set_mode(size)
running = True
ex = Board(9, 7)
ex.set_view(30, 30, 30)
ex.render()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
