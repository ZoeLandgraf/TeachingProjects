from pygame.locals import *
import pygame
import numpy as np

pygame.init()

STEP_SIZE = 10

colors = { "red" : (255,0,0),
           "green" : (0,255,0),
            "white" : (255,255,255),
           "blue" : (0,20,255),
           "orange" : (255,164,0),
           "yellow" : (255,255,0) }


class Ball(pygame.sprite.Sprite):

    def __init__(self, width, height):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colors["white"])
        pygame.draw.rect(self.image, colors["white"], [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
        self.set_velocity()

    def set_velocity(self):
        self.vel_x = np.random.uniform(-2,2) * 5
        self.vel_y = 8


    def reverse_sign(self, value):
        if value > 0:
            return -1
        return 1

    def bounce_off_brick(self):
        self.vel_x = self.vel_x * np.random.uniform(0.5,1.5)
        self.vel_y = self.reverse_sign(self.vel_y) * abs(self.vel_y)

    def bounce_off_walls(self, width, height):
        # Check if the ball is bouncing against any of the 4 walls:
        if self.rect.x >= width:
            self.vel_x = -self.vel_x
        if self.rect.x <= 0:
            self.vel_x = -self.vel_x
        if self.rect.y > height:
            self.vel_y = -self.vel_y
        if self.rect.y <= 0:
            self.vel_y = -self.vel_y

    def hit_floor(self, height):
        if self.rect.y > height:
            return True
        return False

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class Paddle(pygame.sprite.Sprite):

    def __init__(self, width, height):

        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colors["green"])
        pygame.draw.rect(self.image, colors["green"], [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 550

    def stop_at_walls(self):
        if self.rect.x < 0:
            self.rect.x += STEP_SIZE
        if self.rect.x > 700:
            self.rect.x -= STEP_SIZE


class Brick(pygame.sprite.Sprite):

    def __init__(self, posx, posy, color):

        super().__init__()

        self.color = color
        self.image = pygame.Surface([80, 10])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

class Environment():

    def __init__(self, wHeight=600, wWidth=800):
        # display width and height
        self.windowWidth = wWidth
        self.windowHeight = wHeight

        # appearance
        self.display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Game name')
        self.paddle = Paddle(100,10)
        self.ball = Ball(10,10)

        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.ball)
        self.all_sprites_list.add(self.paddle)
        self.all_brick_list = pygame.sprite.Group()
        self.set_up_bricks()

        self.lives = 1
        self.score = 0

    def display_lives(self):
        font = pygame.font.Font(None, 40)
        text = font.render("Lives: " + str(self.lives), 1, (255, 255, 255))
        self.display_surf.blit(text, (35, 15))

    def display_score(self):
        font = pygame.font.Font(None, 40)
        text = font.render("Score: " + str(self.score), 1, (255, 255, 255))
        self.display_surf.blit(text, (650, 15))

    def set_up_bricks(self):

        start_x = 45
        start_y = 50
        for j in range(5):
            position_y = start_y + j*30
            for i in range(8):
                position_x = start_x + i * 90
                if j < 1:
                    color = colors['red']
                elif j < 3:
                    color = colors['orange']
                else:
                    color = colors['yellow']

                brick = Brick(position_x, position_y, color)
                self.all_brick_list.add(brick)
                self.all_sprites_list.add(brick)


    def render(self):
        self.display_surf.fill(colors["blue"])

        self.paddle.stop_at_walls()

        self.ball.bounce_off_walls(self.windowWidth, self.windowHeight)

        if pygame.sprite.collide_rect(self.ball, self.paddle):
            self.ball.rect.x -= self.ball.vel_x
            self.ball.rect.y -= self.ball.vel_y
            self.ball.bounce_off_brick()

        # Check if there is a car collision
        brick_collision_list = pygame.sprite.spritecollide(self.ball, self.all_brick_list, False)
        for brick in brick_collision_list:
            self.ball.bounce_off_brick()
            brick.kill()

        self.display_lives()
        self.display_score()

        self.all_sprites_list.update()
        self.all_sprites_list.draw(self.display_surf)
        pygame.display.update()

    def render_lost_screen(self):
        # Display Game Over Message for 3 seconds
        self.display_surf.fill(colors["blue"])
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER", 1, (255, 255, 255))
        self.display_surf.blit(text, (250, 300))
        pygame.display.flip()

    def render_winning_screen(self):
        # Display Game Over Message for 3 seconds
        self.display_surf.fill(colors["blue"])
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WON!", 1, (255, 255, 255))
        self.display_surf.blit(text, (250, 300))
        pygame.display.flip()

def main():
    pygame.init()

    env = Environment()

    running = True
    counter = 0

    while running:
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if (keys[K_RIGHT]):
            env.paddle.rect.x += STEP_SIZE
        if (keys[K_LEFT]):
            env.paddle.rect.x -= STEP_SIZE

        env.render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.quit()
    pygame.quit()

main()






transl;a
