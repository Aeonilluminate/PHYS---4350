import pygame
import math
import numpy as np
pygame.font.init()

WIDTH, HEIGHT = 1000, 600
X_SHIFT, Y_SHIFT = WIDTH // 2, HEIGHT // 2
AXIS_THICKNESS = 2
TICK_LENGTH = 6
TICK_THICKNESS = 2
TICK_INTERVAL = 10

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

AXIS_FONT = pygame.font.SysFont('lucidasans', 20)

X_AXIS = pygame.Rect(0, 2*Y_SHIFT - AXIS_THICKNESS//2, WIDTH, AXIS_THICKNESS)
Y_AXIS = pygame.Rect(AXIS_THICKNESS//2, 0, AXIS_THICKNESS, HEIGHT)

X_TICKS = [pygame.Rect(x, X_AXIS.centery - TICK_LENGTH//2, TICK_THICKNESS, TICK_LENGTH) for x in np.arange(0, WIDTH, TICK_INTERVAL)]
Y_TICKS = [pygame.Rect(Y_AXIS.centerx - TICK_LENGTH//2, y, TICK_LENGTH, TICK_THICKNESS) for y in np.arange(0, HEIGHT, TICK_INTERVAL)]

WHITE = 255*np.ones(3)
BLACK = np.zeros(3)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def throw_projectile(mass, angle, initial_pos, initial_vel, g=9.8):
    pass


def draw_window():
    WIN.fill(WHITE)

    x_label = AXIS_FONT.render('X Axis', 1, RED)
    y_label = AXIS_FONT.render('Y_axis', 1, RED)
    WIN.blit(x_label, np.array(X_AXIS.topright) - np.array((x_label.get_width(), 25)))
    WIN.blit(y_label, np.array(Y_AXIS.topright) + np.array((TICK_LENGTH//2, 0)))

    for axis in [X_AXIS, Y_AXIS]:
        pygame.draw.rect(WIN, BLACK, axis)

    for x_tick in X_TICKS:
        pygame.draw.rect(WIN, BLACK, x_tick)
    for y_tick in Y_TICKS:
        pygame.draw.rect(WIN, BLACK, y_tick)
    
    pygame.display.flip()

def main():

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        draw_window()

        throw_projectile(mass=5, angle=60, initial_pos=(0,0), initial_vel=50)

    main()

if __name__ == '__main__':
    main()