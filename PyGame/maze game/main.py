import time
import pygame
from environment import Environment
from pygame.locals import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    env = Environment()
    while run == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        if env.is_escape_pressed() == True:
            run = False

        env.render()
        clock.tick(10)

    pygame.display.quit()
    pygame.quit()

if __name__ == "__main__":
    main()