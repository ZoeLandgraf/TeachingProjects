import pygame

from Environment import Environment as E
import Environment

def main():

    pygame.init()

    env = E()

    running = True
    clock = pygame.time.Clock()

    while running:

        env.render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        clock.tick(10)


    pygame.display.quit()
    pygame.quit()



if __name__ == "__main__":
    main()