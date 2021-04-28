import pygame
import numpy as np
from pygame.locals import *
import random
import time
from maze import Maze
from player import Player
from enemies import Enemy
from enemies import Stalker
import enemies
class Environment:

    def __init__(self):

        # display width and height
        self.windowWidth = 640
        self.windowHeight = 480

        self.lost_life = pygame.mixer.Sound('/Users/zoelandgraf/Tutoring/PyGame/maz_game_final/mazegame/Images/laser1.wav')

        self.enemycount = 1

        self.enemyposx = 580

        self.enemies  = []
        # appearance
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.RESIZABLE)
        pygame.display.set_caption('Maze')
        pygame.init()
        # control variable to start and stop the game
        self.maze = Maze()
        self.player = Player()


        for enemy in range(self.enemycount):
            currenty = random.randrange(10, self.windowHeight-30, 20)
            self.newenemy = Enemy(self.enemyposx,currenty)
            self.enemies.append(self.newenemy)


        self.stalker = Stalker(barriers = self.maze.barriers,
                               game_dims = (self.windowWidth, self.windowHeight),
                               rows = self.maze.maze.shape[1],
                               cols = self.maze.maze.shape[0])

        self.finished_maze = False

        self.background = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/maz_game_final/mazegame/Images/forestbackground.png')
        self.background = pygame.transform.scale(self.background, (self.windowWidth, self.windowHeight))

    def exit_program(self):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return True
        return False



    def draw_text_middle(self, text, size, color, surface):
        font = pygame.font.SysFont('comicsans', size, bold=True)
        label = font.render(text, 1, color)

        # rendering the text
        surface.blit(label, (150, 200))

    def display_losing_screen(self, win):
            win.fill((255, 255, 255))
            self.draw_text_middle("The race is over for you", 30, (0, 0, 0), win)
            pygame.display.update()

    def display_winning_screen(self, win):
            win.fill((0, 0, 0))
            self.draw_text_middle("Nicely done!", 30, (255, 255, 255), win)
            pygame.display.update()

    def activity(self):
        hit_player = self.stalker.activity()
        if hit_player:
            self.player.lives -= 1
            pygame.mixer.Sound.play(self.lost_life)

        for enemy in self.enemies:
            enemy.activity(self.player)

        if self.maze.intersect_maze(self.player):
            self.player.undo_move()
        self.finished_maze = self.maze.check_for_finish(self.player)
        self.player.hitting_edges(self.windowWidth, self.windowHeight)



    def render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self.background,(0,0))
        self.maze.render(self._display_surf)

        for enemy in self.enemies:
            enemy.render_enemy(self._display_surf)

        self.player.render_player(self._display_surf)

        self.stalker.render(self._display_surf)

        pygame.display.update()



    def update_enemies(self):

        for enemy in self.enemies:
            enemy.check_swap_position()
            enemy.move()





