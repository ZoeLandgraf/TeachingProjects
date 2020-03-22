from pygame.locals import *
import pygame
import numpy as np

class GameSurface:

    def __init__(self):

        # display width and height
        self.windowWidth = 640
        self.windowHeight = 480

        # appearance
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.RESIZABLE)
        pygame.display.set_caption('Maze')

        pygame.init()
        # control variable to start and stop the game
        self._running = True

        self.clock = pygame.time.Clock()

        self.object = pygame.Surface([30,30])
        self.object.fill((225,225,225))


    def check_for_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.KEYDOWN:

                if event.key == K_ESCAPE:
                    self._running = False

    def render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self.object, (200, 200))
        pygame.display.update()


    def run_game(self):
        while self._running == True:
            self.check_for_quit()
            self.render()
            self.clock.tick(50)



if __name__ == "__main__":
    our_game = GameSurface()
    our_game.run_game()




