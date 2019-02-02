import pygame

pygame.init()
x, y = 300, 300
size = width, height = x, y
screen = pygame.display.set_mode(size)
screen.fill((0, 255, 0))
running = True


def draw():
    font = pygame.font.Font(None, 50)
    text = font.render("Game\nOver", 1, (255, 255, 255))
    text_x = 0
    text_y = 0
    text_w = 300
    text_h = 300
    screen.blit(text, (text_x, text_y))
    r = pygame.draw.rect(screen, (0, 0, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20))

while running:
    screen.fill((0, 255, 0))
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.flip()
