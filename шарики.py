import pygame
pygame.init()
w = 800
h = 600
white = (255, 255, 255)
black = (0, 0, 0)
radius = 20
FPS = 50
count_balls = 15
window = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
XY = []
velocity = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos_x, pos_y = event.pos
            speed_x = -100//FPS
            speed_y = -100//FPS
            XY.append([pos_x, pos_y])
            velocity.append([speed_x, speed_y])
    window.fill(black)
    for i in range(len(velocity)):
        XY[i][0] += velocity[i][0]
        XY[i][1] += velocity[i][1]
        if XY[i][0] + radius > w or XY[i][0]-radius < 0:
            velocity[i][0] = -velocity[i][0]
        if XY[i][1] + radius > h or XY[i][1]-radius < 0:
            velocity[i][1] = -velocity[i][1]
        pygame.draw.circle(window, white, XY[i], radius)
    clock.tick(FPS)
    pygame.display.flip()
