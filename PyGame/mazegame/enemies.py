import pygame
from gridsearch_module import GridSearch
import numpy as np

# Homework
# USE FUNCTIONS AT THE BOTTOM OF FILE
#   TO IMPLEMENT THE STALKING, USING OUR GRIDSEARCH MODULE.
#   SCROLL DOWN TO SEE FUNCTIONS
# USE RETURNED PATH POSITIONS FROM GRIDSEARCH MODULE
#   TO MAKE THE STALKER MOVE

class Spear:

    def __init__(self, pos_x, pos_y):

        self.appearance = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/maz_game_final/mazegame/Images/623-6230928_spear-pixel-art-hd-png-download.png')
        self.appearance = pygame.transform.scale(self.appearance,(80, 20))

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.lost_life = pygame.mixer.Sound('/Users/zoelandgraf/Tutoring/PyGame/maz_game_final/mazegame/Images/laser1.wav')

    def move_forward(self, player):
        self.pos_x -= 10
        self.spear_hits_player(player)

    def render(self, display):

        display.blit(self.appearance, (self.pos_x, self.pos_y))

    def spear_hits_player(self, player):
        if self.check_for_overlap(self.pos_x, player.posx) and self.check_for_overlap(self.pos_y, player.posy):
            player.lives -= 1
            pygame.mixer.Sound.play(self.lost_life)

    def check_for_overlap(self, value1, value2):
        if value1 >= value2 and value1 <= value2 + 30:
            return True

class Enemy:

    def __init__(self, xposition, yposition):

        self.posx = xposition
        self.posy = yposition

        self.direction = 'down'

        self.enemyimage = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/maz_game_final/mazegame/Images/goblin.png')
        self.enemyimage = pygame.transform.scale(self.enemyimage, (60, 60))

        self.spears = []


    def render_enemy(self, display):
        display.blit(self.enemyimage, (self.posx, self.posy))
        for spear in self.spears:
            spear.render(display)

    def activity(self, player):
        if self.shoot_new_spear():

            self.spears.append(Spear(self.posx, self.posy + 20))
        self.shoot_spears(player)


    def shoot_new_spear(self):
        l = np.random.randint(0,2, 30)
        # print(l)
        # print (l.sum())
        if l.sum() > 20:
            return True
        return False

    def shoot_spears(self, player):
        for i, spear in enumerate(self.spears):
            if spear.pos_x < 0:
                del self.spears[i]
                continue
            spear.move_forward(player)

class Stalker:
    def __init__(self, barriers, game_dims, rows, cols):
        self.stalker_active = False
        self.stalkerimage = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/maz_game_final/mazegame/Images/vector-bullet-bill-11.png')
        self.stalkerimage = pygame.transform.scale(self.stalkerimage, (30, 30))
        self.grid_posx = None
        self.grid_posy = None
        self.startingpos = (1,1)
        self.goalpos = (0,0)
        self.pathfinder = GridSearch(barriers=barriers,
                                     game_dims=game_dims,
                                     nbr_of_rows=rows,
                                     nbr_of_columns=cols)
        self.path_positions = []
        self.step = 0

    def update_player_position(self, player_position):
        # self.player_positions.append(player_position)
        # SET THE GOAL POSITION HERE
        self.goalpos = self.position_to_grid_id(player_position)
        # transform goal pos into grid indices


    def caught_player(self):
        if (self.grid_posy,self.grid_posx) == self.goalpos:
            return True
        else:
            return False

    def follow_player(self):
        # CALL THE SEARCH AND FOLLOW FUNCTION (TAKES AS INPUT, START AND GOAL POS)
        # IMPORTANT: IN THIS CLASS WE NEED TO JUGGLE THE GRID INDECES AND REAL POSITIONS
        #       WE NEED TO CONSTANTLY TRANSFORM BETWEEN REAL POSITIONS AND GRID POSITIONS
        #       USE THE FUNCTIONS AT THE BOTTOM OF FILE
        length = len(self.path_positions)
        if length == 0:
            self.startingpos = (1,1)
            self.stalker_active = False
            if self.caught_player():
                hit_player = True
            else:
                hit_player = False
            return hit_player
        else:
            self.grid_posy, self.grid_posx = self.path_positions[0]
            self.path_positions = self.path_positions[1:]
            hit_player = False
            return hit_player


    def render(self, display):
        if self.stalker_active:
            real_position = self.grid_id_to_position((self.grid_posx, self.grid_posy))
            display.blit(self.stalkerimage, real_position)

    def activity(self):


        if not self.stalker_active and self.goalpos is not None:
            # check if player has moved
            x,y = self.goalpos
            if x > 3 or y > 3:
                if np.random.randint(0,20) > 16:
                    self.path_positions = self.pathfinder.search_n_follow(self.goalpos, self.startingpos)
                    if len(self.path_positions) > 0:
                        self.stalker_active = True

        if self.stalker_active:
            hit_player = self.follow_player()
            return hit_player

        else:
            return False

    def position_to_grid_id(self, pos):
        grid_id_x = (pos[0] - 90 + 15) // 30
        grid_id_y = (pos[1] - 40 + 15) // 30
        return (grid_id_y, grid_id_x)

    def grid_id_to_position(self, pos):
        pos_x = (pos[0] * 30) + 90
        pos_y = (pos[1] * 30) + 40
        return (pos_x - 15, pos_y - 15)



