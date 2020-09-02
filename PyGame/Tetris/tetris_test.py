# Libraries required
import pygame
import random
import numpy as np
pygame.font.init()


def create_grid(x, y, locked_positions={}):
    grid = [[(0, 0, 0) for _ in range(x)] for _ in range(y)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid




def main(win):

    run = True
    while run:
        # Filling the window with black (0,0,0) pixels
        win.fill((0, 0, 0))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


# Using pygame to create a window and initialiize it
s_width = 800
s_height = 800

win = pygame.display.set_mode((s_width, s_height))
pygame.display.init()

# Setting the caption of our game
pygame.display.set_caption('Tetris')

main(win)