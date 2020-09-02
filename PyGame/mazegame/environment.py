import pygame
import numpy as np
from pygame.locals import *
import random
import time
from maze import Maze
from player import Player
from enemies import Enemy
from enemies import Stalker

class Environment:

    def __init__(self):

        # display width and height
        self.windowWidth = 640
        self.windowHeight = 480

        # appearance
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.RESIZABLE)
        pygame.display.set_caption('Maze')
        pygame.init()
        # control variable to start and stop the game
        self.maze = Maze()
        self.player = Player()

        self.startingposx = 100
        self.enemy = Enemy(580, 240)

        self.stalker = Stalker()


        self.background = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/mazegame/Images/forestbackground.png')
        self.background = pygame.transform.scale(self.background, (self.windowWidth, self.windowHeight))

    def exit_program(self):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return True
        return False


    def render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self.background,(0,0))
        self.maze.render(self._display_surf)

        self.player.render_player(self._display_surf)

        self.enemy.activity(self.player)
        self.enemy.render_enemy(self._display_surf)

        hit_player = self.stalker.activity()
        if hit_player:
            self.player.lives -= 1

        self.stalker.render(self._display_surf)

        self.maze.check_for_finish(self.player)

        if self.maze.intersect_maze(self.player):
            self.player.undo_move()

        self.player.hitting_edges(self.windowWidth, self.windowHeight)
        pygame.display.update()

    def update_enemies(self):

        for enemy in self.enemies:
            enemy.check_swap_position()
            enemy.move()





