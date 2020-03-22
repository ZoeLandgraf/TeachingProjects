import pygame
from game_environment import Environment

def main():

    pygame.init()
    env = Environment()
    playing_game = True

    while playing_game:

        env.render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing_game = False


if __name__ == "__main__":
    main()