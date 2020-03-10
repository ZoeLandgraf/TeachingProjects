from pygame.locals import *
import pygame
import numpy as np

class Snake:

    def __init__(self,
                 screen_width,
                 screen_height,
                 initial_position_x=30,
                 initial_position_y=30):

        self.body_x = []
        self.body_y = []
        self.piece_size = 30

        self.log = False

        self.length = 3

        self.colour = (255, 0, 0)
        self.surface = pygame.Surface([self.piece_size, self.piece_size])
        self.surface.fill((255, 0, 0))

        # add direction member variable (we encode directions as numbers 0-3, 0 being right)
        self.direction = 0


        self.setup_snake(initial_position_x, initial_position_y)

        self.snake_head_x = initial_position_x
        self.snake_head_y = initial_position_y

        self.screen_width = screen_width
        self.screen_height = screen_height


    def setup_snake(self, initial_position_x, initial_position_y):

        # Fill the head of the snake body with the initial position.
        # This segment is the equivalent of the snake's head
        self.body_x.append(initial_position_x)
        self.body_y.append(initial_position_y)

        for i in range(1,self.length):
            previous_position = self.body_x[i-1]
            self.body_x.append(previous_position - self.piece_size)

        for i in range(1,self.length):
            previous_position = self.body_y[i-1]
            self.body_y.append(previous_position)


    def reverse(self):
        # This reverses the order of the snake body,
        # making the tail end the head
        self.body_x.reverse()
        self.body_y.reverse()

    def update_direction(self, direction):
        # ensure valid direction
        if direction < 0 or direction > 3:
            direction = 0

        # reverse snake if position is switched
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

        for i in range(self.length - 1, 0, -1):
            self.body_x[i] = self.body_x[i - 1]
            self.body_y[i] = self.body_y[i - 1]

        self.body_x[0] = self.snake_head_x
        self.body_y[0] = self.snake_head_y

    def extend_snake(self):

        self.length += 1

        new_snake_x = np.zeros(self.length)
        new_snake_y = np.zeros(self.length)

        self.move(update_position=False)

        new_snake_x[0]=self.snake_head_x
        new_snake_y[0]=self.snake_head_y

        new_snake_x[1:] = self.body_x
        new_snake_y[1:] = self.body_y

        self.body_x = list(new_snake_x)
        self.body_y = list(new_snake_y)


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
        self.snake_head_x = self.snake_head_x + self.piece_size

    def moveLeft(self):
        self.snake_head_x = self.snake_head_x - self.piece_size

    def moveUp(self):
        self.snake_head_y = self.snake_head_y - self.piece_size

    def moveDown(self):
        self.snake_head_y = self.snake_head_y + self.piece_size

    def appearance(self):
        return self.surface

    def location(self):
        # Return the entire snake body.
        return [(el[0], el[1]) for el in zip(self.body_x, self.body_y)]


class Apple:
    def __init__(self,
                 windowwidth, windowheight):

        self.surface = pygame.Surface([30, 30])
        self.surface.fill((44, 135, 60))
        self.posx = np.random.choice(range(0, windowwidth, 30))
        self.posy = np.random.choice(range(0, windowheight, 30))
        self.windowwidth = windowwidth
        self.windowheight = windowheight

    def get_position(self):
        return (self.posx, self.posy)

    def generate_position(self):
        self.posx = np.random.choice(range(0, self.windowwidth, 30))
        self.posy = np.random.choice(range(0, self.windowheight, 30))


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


class GameSurface:

    def __init__(self):

        # display width and height
        self.windowWidth = 600
        self.windowHeight = 600

        # snake
        self.snake = Snake(self.windowWidth, self.windowHeight)

        # appearance
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Snake')

        pygame.init()
        # control variable to start and stop the game
        self._running = True

        self.clock = pygame.time.Clock()
        self.apple = Apple(windowwidth=self.windowWidth, windowheight=self.windowHeight)

    def check_for_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

    def check_for_loss(self):
        out_of_limits_max = self.snake.snake_head_x > self.windowWidth or self.snake.snake_head_y > self.windowHeight
        out_of_limits_min = self.snake.snake_head_x < 0 or self.snake.snake_head_y < 0

        if (out_of_limits_max is True) or (out_of_limits_min is True):
           return True

        if (self.snake.snake_head_x in self.snake.body_x is True) or (self.snake.snake_head_y in self.snake.body_x is True):
           return True

        return False

    def render(self):
        self._display_surf.fill((0, 0, 0))
        # view snake
        snake_appearance = self.snake.appearance()
        snake_location = self.snake.location()
        apple_appearance = self.apple.surface
        apple_location = self.apple.get_position()

        # draw every segment in the snake body onto the gaming screen
        for el in snake_location:
            self._display_surf.blit(snake_appearance, el)
        self._display_surf.blit(apple_appearance, apple_location)
        # updates the display
        drawGrid(600, 20, self._display_surf)
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

            if (self.apple.posx == self.snake.snake_head_x) and (self.apple.posy == self.snake.snake_head_y):
                self.apple.generate_position()
                self.snake.extend_snake()

            self.snake.move()

            # instead of moving the snake with the arrowkeys, we now set its direction
            if (keys[K_RIGHT]):
                self.snake.update_direction(0)

            if (keys[K_LEFT]):
                self.snake.update_direction(2)

            if (keys[K_UP]):
                self.snake.update_direction(3)

            if (keys[K_DOWN]):
                self.snake.update_direction(1)

            # if self.snake.snake_head_x == self.apple.posx and self.snake.snake_head_y == self.apple.posy:
            if self.check_for_loss() == True:
                self._running = False


            self.check_for_quit()
            self.render()

            self.clock.tick(10)

        for i in range(100):
            print(i)
            pygame.time.delay(30)
            self._display_surf.fill((225, 30, 0))
            # font = pygame.font.Font(None, 60)
            # text = font.render("You lost.", 1, (0, 0, 0))
            # self._display_surf.blit(text, (300, 250))
            pygame.display.update()
            pygame.time.delay(30)
            self.clock.tick(10)

        self.cleanup()


if __name__ == "__main__":
    our_game = GameSurface()
    our_game.play_game()