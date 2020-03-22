import pygame


class Environment:

    def __init__(self, wHeight= 600, wWidth=800):
        # display width and height
        self.windowWidth = wWidth
        self.windowHeight = wHeight

        # appearance
        self.display_surface = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Game name')


    def render(self):
        self.display_surf.fill((0,200,0))
        pygame.display.update()