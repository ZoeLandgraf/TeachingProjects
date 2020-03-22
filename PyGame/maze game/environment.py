import pygame
from pygame.locals import *

class Environment:

    def __init__(self):

        # display width and height
        self.windowWidth = 640
        self.windowHeight = 480

        # appearance
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Maze')

        pygame.init()
        # control variable to start and stop the game


        self.object = pygame.Surface([30,30])
        self.object.fill((225,225,225))

    def is_escape_pressed(self):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
           return True

        return False

    def render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self.object, (200, 200))
        pygame.display.update()