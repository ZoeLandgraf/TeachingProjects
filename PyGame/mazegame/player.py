import pygame
import random
from random import randint
import time
# h o m e w o r k   f o r   J u n e   17 ,   2 0 2 0
# add a range for the finish line. (<= >=)
# finish the winning (and losing) screen
# add other enemies
#

class Player:

    def __init__(self):

        self.posx = 30
        self.posy = 30


        self.lives = 30
        self.score = 0
        self.grace_period = False
        self.player = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/mazegame/Images/340220dd000a8af.png')
        self.player = pygame.transform.scale(self.player,(30,30))
        self.last_movement = 0

    def render_player(self, display):
        display.blit(self.player, (self.posx, self.posy))
        self.draw_text_lives(display)


    def hitting_edges(self, dimensionx, dimensiony):
        if self.posx >= dimensionx - 30:
            self.posx-= 10
        if self.posy >= dimensiony - 30:
            self.posy-= 10
        if self.posx <= 0:
            self.posx += 10
        if self.posy <= 0:
            self.posy += 10


    def reset_player_position(self, windowHeight):
        self.posx = random.randrange(20, 50, 10)
        self.posy = random.randrange(20, windowHeight - 20, 10)


    def update_position(self,code):
        if code == 0:
            self.posx+=10
        if code == 1:
            self.posy+=10
        if code == 2:
            self.posx-=10
        if code == 3:
            self.posy-=10
        self.last_movement = code


    def undo_move(self):
        if self.last_movement == 0:
            self.posx-=10
        if self.last_movement == 1:
            self.posy-=10
        if self.last_movement == 2:
            self.posx+=10
        if self.last_movement == 3:
            self.posy+=10


    def draw_text_lives(self, surface):
        font = pygame.font.SysFont('timesnewroman', 30, bold=False)

        sx = self.posx - 60
        sy = self.posy + 50

        label = font.render( 'Hearts:', 1, (255, 255, 255))
        surface.blit(label, (sx, sy))

        life_value = font.render(str(self.lives), 1, (255, 255, 255))
        surface.blit(life_value, (sx, sy + 20))

    def draw_text_score(self, surface):
        font = pygame.font.SysFont('comicsans', 30, bold=False)

        s2x = 20
        s2y = 10

        label = font.render('score:', 1, (255, 255, 255))
        surface.blit(label, (s2x, s2y))

        score_value = font.render(str(self.score), 1, (255, 255, 255))
        surface.blit(score_value, (s2x + 60, s2y))
