from pygame.locals import *
import pygame

class Snake:

    def __init__(self,
                 initial_speed=1,
                 initial_position_x=10,
                 initial_position_y=10):
        self.x = initial_position_x
        self.y = initial_position_y
        self.speed_multiplier = 0.1

        self.speed = initial_speed
        self.step = self.speed_multiplier * self.speed

        self.length = 1

        self.colour = (255, 0, 0)
        self.surface = pygame.Surface([15, 15])
        self.surface.fill((255, 0, 0))

    def moveRight(self):
        self.x = self.x + self.step

    def moveLeft(self):
        self.x = self.x - self.step

    def moveUp(self):
        self.y = self.y - self.step

    def moveDown(self):
        self.y = self.y + self.step

    def appearance(self):
        return self.surface

    def location(self):
        return (self.x, self.y)

class GameSurface:
    windowWidth = 800
    windowHeight = 600
    player = 0

    def __init__(self,
                 initial_speed):

        # display width and height
        self.windowWidth = 800
        self.windowHeight = 600

        # snake
        self.snake = Snake(initial_speed)

        # appearance
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Snake')

        pygame.init()
        # control variable to start and stop the game
        self._running = True

    def check_for_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

    def render(self):
        self._display_surf.fill((0, 0, 0))
        # view snake
        snake_appearance = self.snake.appearance()
        snake_location = self.snake.location()
        self._display_surf.blit(snake_appearance, snake_location)
        # updates the display
        pygame.display.flip()

    def on_cleanup(self):
        pygame.display.quit()
        pygame.quit()

    def play_game(self):

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.snake.moveRight()

            if (keys[K_LEFT]):
                self.snake.moveLeft()

            if (keys[K_UP]):
                self.snake.moveUp()

            if (keys[K_DOWN]):
                self.snake.moveDown()

            self.check_for_quit()
            self.render()
        self.on_cleanup()


if __name__ == "__main__":
    our_game = GameSurface(initial_speed=1)
    our_game.play_game()