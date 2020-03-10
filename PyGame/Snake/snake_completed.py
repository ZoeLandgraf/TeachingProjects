from pygame.locals import *
import pygame
import numpy as np


class Snake:

    def __init__(self,
                 screen_width,
                 screen_height,
                 initial_position_x = 10,
                 initial_position_y = 10):

        self.x = []
        self.y = []

        self.log = False

        self.length = 5

        # if this is not 1, the snake will be offset from the grid and won't be able to catch the apple
        self.slow_down = 1;

        self.colour = (255 ,0 ,0)
        self.surface = pygame.Surface([10, 10])
        self.surface.fill((255 ,0 ,0))

        # add direction member variable (we encode directions as numbers 0-3, 0 being right)
        self.direction = 0
        self.piece_size = 10

        self.setup_snake(initial_position_x, initial_position_y)

        self.snake_head_x = initial_position_x
        self.snake_head_y = initial_position_y

        self.screen_width = screen_width
        self.screen_height = screen_height

    def setup_snake(self, initial_position_x, initial_position_y):
        self.x = [initial_position_x - i * self.piece_size * self.slow_down for i in range(self.length)]
        self.y = [initial_position_y for _ in range(self.length)]

    def reverse(self):
        # This reverses the order of the snake body,
        # making the tail end the head
        self.x.reverse()
        self.y.reverse()

    def update_direction(self, direction):
        # ensure valid direction
        if direction < 0 or direction > 3:
            direction = 0

        #reverse snake if position is switched
        if abs(direction - self.direction) == 2:
            self.reverse()

        self.direction = direction

    def update_snake_position(self):

        # UPDATE THE SNAKE's BODY
        # Here, we iterate through our snake's body, step by step
        # moving every snake segment one step forward.
        # Why do we need to update the snake body in reverse?
        # Because, if we started at the snake's head, then every next segment
        # would be updated with the same location.

        for i in range(self.length-1,0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        self.x[0] = self.snake_head_x
        self.y[0] = self.snake_head_y


    # The move function, which moves the snake depending on the direction that it currently has
    def move(self, update_position=True):
        if self.direction == 0:
            self.moveRight()
        elif self.direction == 1:
            self.moveDown()
        elif self.direction == 2:
            self.moveLeft()
        elif self.direction == 3:
            self.moveUp()

        if update_position:
            self.update_snake_position()

    def moveRight(self):
        self.snake_head_x = self.snake_head_x + (self.piece_size * self.slow_down)

    def moveLeft(self):
        self.snake_head_x = self.snake_head_x - (self.piece_size * self.slow_down)

    def moveUp(self):
        self.snake_head_y = self.snake_head_y - (self.piece_size * self.slow_down)

    def moveDown(self):
        self.snake_head_y = self.snake_head_y + (self.piece_size * self.slow_down)

    def appearance(self):
        return self.surface

    def location(self):
        # Return the entire snake body.
        return [(el[0], el[1]) for el in zip(self.x, self.y)]

    def extendsnake(self):
        """
        TODO
        :param length:
        :return:
        """
        self.length += 1

        new_snake_x = np.zeros(self.length)
        new_snake_y = np.zeros(self.length)

        self.move(update_position=False)

        new_snake_x[0] = self.snake_head_x
        new_snake_y[0] = self.snake_head_y

        new_snake_x[1:] = self.x
        new_snake_y[1:] = self.y

        self.x = list(new_snake_x)
        self.y = list(new_snake_y)

class GameSurface:

    def __init__(self
                 ):

        # display width and height
        self.windowWidth = 800
        self.windowHeight = 600

        # snake
        self.snake = Snake(self.windowWidth, self.windowHeight)
        self.apple_surface = pygame.Surface([10, 10])
        self.apple_surface.fill((0, 255, 0))
        self.randomly_place_apple()

        # appearance
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Snake')

        pygame.init()
        # control variable to start and stop the game
        self._running = True

        self.delay=1

    def randomly_place_apple(self):
        # The apple has to be placed in positions of interval 10 if this is the interval at which the snake moves
        self.apple_position = (np.random.choice([i for i in range(0, self.windowWidth, 10)]), \
                               np.random.choice([i for i in range(0, self.windowHeight, 10)]))

    def check_for_ate_apple(self):
        if ((self.snake.snake_head_x, self.snake.snake_head_y) == self.apple_position):
            self.randomly_place_apple()
            self.snake.extendsnake()

    def check_for_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

    def render(self):
        self._display_surf.fill((0, 0, 0))
        # view snake
        snake_appearance = self.snake.appearance()
        snake_location = self.snake.location()

        # draw every segment in the snake body onto the gaming screen
        for el in snake_location:
            self._display_surf.blit(snake_appearance, el)

        # show the apple
        self._display_surf.blit(self.apple_surface, self.apple_position)
        # updates the display
        pygame.display.flip()

    def cleanup(self):
        pygame.display.quit()
        pygame.quit()



    def play_game(self):
        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()


            # always move the snake. As the initial direction is set to 0, the snake
            # will always start moving right.
            self.snake.move()

            self.check_for_ate_apple()

            # instead of moving the snake with the arrowkeys, we now set its direction
            if (keys[K_RIGHT]):
                self.snake.update_direction(0)

            if (keys[K_LEFT]):
                self.snake.update_direction(2)

            if (keys[K_UP]):
                self.snake.update_direction(3)

            if (keys[K_DOWN]):
                self.snake.update_direction(1)

            self.check_for_quit()
            self.render()

            pygame.time.delay(self.delay)

        self.cleanup()

if __name__ == "__main__":
    our_game = GameSurface()
    our_game.play_game()