import numpy as np
import pygame
import player

class Maze:
    def __init__(self):
        self.barriers = []
        self.tree = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/maz_game_final/mazegame/Images/tree.png')
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
        self.finish_line = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/maz_game_final/mazegame/Images/261-2613414_clip-art-finish-flag-finish-line-pixel-art.png')
        self.finish_line = pygame.transform.scale(self.finish_line, (70,100))
        self.finishx = 480
        self.finishy = 410


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
                    display.blit(self.tree, (positionx-25, positiony-25))

        display.blit(self.finish_line, (self.finishx, self.finishy))

    def fill_wall_pieces(self):
        startx = 90
        starty = 40
        rows = self.maze.shape[0]
        columns = self.maze.shape[1]
        for row in range(rows):
            for col in range(columns):
                value = self.maze[row][col]
                if value == 1:
                    positionx = startx + col * 30
                    positiony = starty + row * 30
                    self.maze_wall_pieces.append((positionx, positiony))
                    self.barriers.append((row, col))

    def check_for_finish(self, player):
        intersect_x = (self.finishx) <= player.posx and (self.finishx + 70) >= player.posx
        intersect_y = (self.finishy) <= player.posy and (self.finishx + 100) >= player.posy
        if intersect_x and intersect_y:
            return True
        return False



    def intersect_maze(self, player):
        for piece in self.maze_wall_pieces:
            a = (player.posx+15) > piece[0] - 25
            b = (player.posx+15) < piece[0] + 25
            c = (player.posy+15) > piece[1] - 25
            d = (player.posy+15) < piece[1] + 25

            if a and b and c and d:
                return True

        return False

    def draw_text_middle(self, text, size, color, surface):
        font = pygame.font.SysFont('comicsans', size, bold=True)
        label = font.render(text, 1, color)

        # rendering the text
        surface.blit(label, (150, 200))