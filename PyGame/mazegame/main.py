import time
import pygame
from environment import Environment
from pygame.locals import *
from maze import Maze
from Button import Button

def game_intro():
    intro = True
    clock = pygame.time.Clock()
    height = 100
    width = 200
    xpos = 640/2 - width/2
    ypos = 480/2 - height/2
    display = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
    gamequit = False

    button = Button((xpos, ypos, width, height))
    while intro:
        display.fill((0,0,0))
        button.render(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                gamequit = True
            if button.mouse_clicked(event):
                intro = False

        pygame.display.update()
        clock.tick(15)
    return gamequit
def maze_game():
    play = True
    theme_song = pygame.mixer.Sound(
        '/Users/zoelandgraf/Tutoring/PyGame/maz_game_final/mazegame/Images/SLOWER-TEMPO2019-12-09_-_Retro_Forest_-_David_Fesliyan.wav')
    counter = 0
    display = True
    clock = pygame.time.Clock()
    run = True
    env = Environment()

    while run:
        if play:
            # pygame.mixer.music.load('/Users/michaelquintin/Desktop/All/programming/ProgrammingZoe/mazegame/Images/SLOWER-TEMPO2019-12-09_-_Retro_Forest_-_David_Fesliyan.wav')
            # pygame.mixer.music.play(-1)
            pygame.mixer.Sound.play(theme_song)
            play = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #print (grace_period_counter)

        keys = pygame.key.get_pressed()

        if keys[K_RIGHT] and keys[K_DOWN]:
            continue

        if keys[K_LEFT] and keys[K_DOWN]:
            continue

        if keys[K_RIGHT] and keys[K_UP]:
            continue

        if keys[K_LEFT] and keys[K_UP]:
            continue
        if display:

            if (keys[K_RIGHT]):
                env.player.update_position(0)
                env.stalker.update_player_position((env.player.posx, env.player.posy))

            if (keys[K_LEFT]):
                env.player.update_position(2)
                env.stalker.update_player_position((env.player.posx, env.player.posy))

            if (keys[K_UP]):
                env.player.update_position(3)
                env.stalker.update_player_position((env.player.posx, env.player.posy))

            if (keys[K_DOWN]):
                env.player.update_position(1)
                env.stalker.update_player_position((env.player.posx, env.player.posy))

        if env.exit_program() == True:
            run = False

        if env.finished_maze:
            env.display_winning_screen(env._display_surf)
            counter+=1
            display = False
        elif env.player.lives > 0:
            env.render()
            env.activity()
        else:
            env.display_losing_screen(env._display_surf)
            counter += 1
            display = False


        clock.tick(10)

        if counter == 50:
            break
    pygame.mixer.pause()


def main():
    pygame.init()


    while True:
        quitgame = game_intro()
        if quitgame:
            break
        maze_game()


    pygame.display.quit()
    pygame.quit()



if __name__ == "__main__":
    main()