import pygame

from Player import Player



class Block:

    def __init__(self, height=5, width=1):

        self.surface = pygame.Surface((width, height))
        self.surface.fill((200,200,60))

class Labyrinth:

    def __init__(self):


        self.components = {Block(height=15, width=150) : (40,55),
                           Block(height=15, width=150) : (195,55),
                           Block(height=15, width=150) : (350,55),

                           Block(height = 150, width=15 ) : (40, 110),
                           Block(height=150, width=15): (40, 265),
                           Block(height=150, width=15): (40, 420),

                           Block(height=15, width=150): (40, 575),
                           Block(height=15, width=150): (195, 575),
                           Block(height=15, width=150): (350, 575),

                           Block(height=15, width=150): (60, 110),
                           Block(height=15, width=150): (215, 110),
                           Block(height=15, width=50): (370, 110),

                           }

    def render(self, surface):

        for el in self.components.items():
            surface.blit(el[0].surface, el[1])


class Environment:

    def __init__(self, wHeight= 600, wWidth=800):
        # display width and height
        self.windowWidth = wWidth
        self.windowHeight = wHeight

        # appearance
        self.display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('NoName')

        self.font = pygame.font.Font(None, 30)


        self.player = Player(lives=3)
        self.labyrinth = Labyrinth()


    def render(self):

        self.display_surf.fill((0,200,0))


        # display lives and score
        text_score = self.font.render("Score: " + str(self.player.score), 1, (255, 255, 255))
        self.display_surf.blit(text_score, (20, 20))


        text = self.font.render("Lives: " + str(self.player.lives), 1, (255, 255, 255))
        self.display_surf.blit(text, (690, 20))

        self.labyrinth.render(self.display_surf)

        pygame.display.update()