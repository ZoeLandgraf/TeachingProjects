
#
# class Environment:
#
#     def __init__(self):
#
#         # display width and height
#         self.windowWidth = 640
#         self.windowHeight = 480
#
#         # appearance
#         self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
#         pygame.display.set_caption('Maze')
#
#         pygame.init()
#         # control variable to start and stop the game
#
#
#         self.object = pygame.Surface([30,30])
#         self.object.fill((225,225,225))
#
#
# def main():
#     pygame.init()
#     clock = pygame.time.Clock()
#     run = True
#     env = Environment()
#     while run == True:
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#
#
#         if env.is_escape_pressed() == True:
#             run = False
#
#         env.render()
#         clock.tick(10)
#
#     pygame.display.quit()
#     pygame.quit()
#
# if __name__ == "__main__":
#     main()


import pygame


