import pygame
import numpy as np

class Environment:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('FlappyBird')
        self.background_1 = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/flappy_bird/flappy-bird-background-1.jpg')

        self.pipes_1 = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/flappy_bird/flappy-bird-pipes.png')
        self.background_1 = pygame.transform.scale(self.background_1, (self.width, self.height))
        self.pipes_1 = pygame.transform.scale(self.pipes_1, (self.width, self.height + 150))
        self.pipes_2 = pygame.transform.scale(self.pipes_1, (self.width, self.height + 150))
        self.bird = pygame.image.load('/Users/zoelandgraf/Tutoring/PyGame/flappy_bird/flappy_bird.png')
        self.bird = pygame.transform.scale(self.bird, (50,50))

        self.bg_1_pos = 0
        self.bg_2_pos = self.width


        self.pipe_1_loc_x = np.random.randint(0, self.width)
        self.pipe_2_loc_x = np.random.randint(self.pipe_1_loc_x + 70, self.width*2)
        self.pipe_1_loc_y = np.random.uniform(-10, -45)
        self.pipe_2_loc_y = np.random.uniform(-10, -45)

        self.pipes_loc = [[self.pipe_1_loc_x, self.pipe_1_loc_y],
                          [self.pipe_2_loc_x, self.pipe_2_loc_y]]

    def update_background(self):
        self.bg_1_pos -= 5
        self.bg_2_pos -= 5

        self.pipes_loc[0][0] -= 5
        self.pipes_loc[1][0] -= 5

        if self.bg_1_pos < -self.width:
            self.bg_1_pos = self.bg_2_pos + self.width

        if self.bg_2_pos < -self.width:
            self.bg_2_pos = self.bg_1_pos + self.width


        first_pipe = self.pipes_loc[0]
        x = first_pipe[0]
        if x < (-self.width / 2):
            new_pipes_loc = []
            new_pipes_loc.append(self.pipes_loc[1])

            # place pipe randomly
            second_pipe_x = np.random.randint(new_pipes_loc[0][0] + 70, self.width*2)
            second_pipe_y = np.random.uniform(-10, -45)
            new_pipes_loc.append([second_pipe_x, second_pipe_y])

            self.pipes_loc = new_pipes_loc

    def render(self):
        self.display.fill((0,0,0))
        self.display.blit(self.background_1,(self.bg_1_pos,0))
        self.display.blit(self.background_1,(self.bg_2_pos,0))


        self.display.blit(self.pipes_1,(self.pipes_loc[0][0],self.pipes_loc[0][1]))
        self.display.blit(self.pipes_1,(self.pipes_loc[1][0],self.pipes_loc[1][1]))

        self.display.blit(self.bird, (50,50))
        self.update_background()
        pygame.display.update()

def main():

    pygame.init()

    env = Environment(600,400)
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        env.render()

main()