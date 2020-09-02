import time
import pygame
from environment import Environment
from pygame.locals import *
from maze import Maze


class Button:
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)
        self.image = pygame.Surface(self.rect.size).convert()
        self.color = (0,150,0)
        self.color_hovering = (0,255,0)


        self.font = pygame.font.SysFont('Arial', 40)
        self.font_color = pygame.Color('white')
        self.text = self.text = self.font.render("Start Game",True,self.font_color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.on_click(event)
        return False

    def is_hovering(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            return True
        return False

    def draw(self, surf):
        if self.is_hovering():
            self.image.fill(self.color_hovering)
        else:
            self.image.fill(self.color)
        surf.blit(self.image, self.rect)
        surf.blit(self.text, self.text_rect)


def run_start_screen(width, height):
    screen = pygame.display.set_mode((width, height))
    done = False
    button_width = 200
    button_height = 100
    btn = Button(rect=((width / 2) - button_width / 2 ,
                       (height / 2) - button_height / 2,
                       button_width, button_height))
    play_game = True
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play_game = False
                done = True

            if btn.get_event(event):
                done = True

        btn.draw(screen)
        pygame.display.update()

    return play_game


def game_loop():

    env = Environment()
    clock = pygame.time.Clock()
    run = True

    while run == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[K_RIGHT] and keys[K_DOWN]:
            continue

        if keys[K_LEFT] and keys[K_DOWN]:
            continue

        if keys[K_RIGHT] and keys[K_UP]:
            continue

        if keys[K_LEFT] and keys[K_UP]:
            continue


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
        env.render()
        clock.tick(10)


def main():
    pygame.init()

    while True:

        play = run_start_screen(640, 480)

        if not play:
            break
        else:
            game_loop()



if __name__ == "__main__":
    main()