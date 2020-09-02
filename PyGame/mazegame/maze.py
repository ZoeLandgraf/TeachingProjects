import numpy as np
import pygame
import player

class Maze:
    def __init__(self):
        self.tree = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/mazegame/Images/tree.png')
        self.tree = pygame.transform.scale(self.tree,(50,50))
        self.maze = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                              [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
                              [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1],
                              [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
                              [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                              [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                              [1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                              [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                              [1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
                              [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                              [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]])
        self.maze_wall_pieces = []
        self.fill_wall_pieces()
        self.finish_line = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/mazegame/Images/261-2613414_clip-art-finish-flag-finish-line-pixel-art.png')
        self.finish_line = pygame.transform.scale(self.finish_line, (70,100))
        self.finishx = 480
        self.finishy = 410
        self.finished_maze = False


    def render(self, display):
        startx = 90
        starty = 40
        rows = self.maze.shape[0]
        columns = self.maze.shape[1]
        for row in range(rows):
            for col in range (columns):
                value = self.maze[row][col]
                if value == 1:
                    positionx = startx+col*30
                    positiony = starty+row*30
                    display.blit(self.tree, (positionx-20, positiony-20))

        display.blit(self.finish_line, (self.finishx, self.finishy))

    def fill_wall_pieces(self):
        startx = 40
        starty = 10
        rows = self.maze.shape[0]
        columns = self.maze.shape[1]
        for row in range(rows):
            for col in range(columns):
                value = self.maze[row][col]
                if value == 1:
                    positionx = startx + col * 30
                    positiony = starty + row * 30
                    self.maze_wall_pieces.append((positionx, positiony))

    def check_for_finish(self, player):
        if (self.finishx + 30) == player.posx and self.finishy == player.posy:
            self.finished_maze = True
            print("yay well done")


    def intersect_maze(self, player):
        for piece in self.maze_wall_pieces:
            a = player.posx > piece[0] + 10
            b = player.posx < piece[0] + 60
            c = player.posy > piece[1]
            d = player.posy < piece[1] + 40

            if a and b and c and d:
                return True

        return False