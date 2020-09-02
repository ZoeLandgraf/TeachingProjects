import pygame
import numpy as np

class Spear:

    def __init__(self, pos_x, pos_y):

        self.appearance = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/mazegame/Images/623-6230928_spear-pixel-art-hd-png-download.png')
        self.appearance = pygame.transform.scale(self.appearance,(80, 20))

        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_forward(self, player):
        self.pos_x -= 10
        self.spear_hits_player(player)

    def render(self, display):

        display.blit(self.appearance, (self.pos_x, self.pos_y))

    def spear_hits_player(self, player):
        if self.check_for_overlap(self.pos_x, player.posx) and self.check_for_overlap(self.pos_y, player.posy):
            player.lives -= 1

    def check_for_overlap(self, value1, value2):
        if value1 >= value2 and value1 <= value2 + 30:
            return True

class Enemy:

    def __init__(self, xposition, yposition):

        self.posx = xposition
        self.posy = yposition

        self.direction = 'down'

        self.enemyimage = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/mazegame/Images/goblin.png')
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
        l = np.random.randint(0,2, 10)
        # print(l)
        # print (l.sum())
        if l.sum() > 7:
            return True
        return False

    def shoot_spears(self, player):
        for i, spear in enumerate(self.spears):
            if spear.pos_x < 0:
                del self.spears[i]
                continue
            spear.move_forward(player)

class Stalker:
    def __init__(self):
        self.player_positions = []
        #start when player has moved x amount from original position
        self.player_positions_limit = 500
        self.start_stalking = 10
        self.stalker_active = False
        self.stalkerimage = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/mazegame/Images/vector-bullet-bill-11.png')
        self.stalkerimage = pygame.transform.scale(self.stalkerimage, (30, 30))
        self.posx = None
        self.posy = None


    def update_player_position(self, player_position):
        self.player_positions.append(player_position)


    def follow_player(self):
        if len(self.player_positions) > 0:
            last_player_position = self.player_positions[0]
            self.posx = last_player_position[0]
            self.posy = last_player_position[1]
            self.player_positions = self.player_positions[1:]
            return False
        else:
            self.stalker_active = False
            return True


    def render(self, display):
        if self.stalker_active:
            display.blit(self.stalkerimage, (self.posx, self.posy))

    def activity(self):
        if len(self.player_positions) > self.start_stalking:
            self.stalker_active = True

        if self.stalker_active:
            hit_player = self.follow_player()
            return hit_player
        else:
            return False






