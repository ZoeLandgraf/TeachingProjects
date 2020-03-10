import pygame
pygame.init()

# Define some colors
WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)


clock = pygame.time.Clock()

# Open a new window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Drawer")
carry_on = True

pencil = pygame.Surface([10, 10])
pencil.fill(WHITE)
pencil_location = (500,200)
point_start = pencil_location
point_end = pencil_location

def draw_a_line(screen, point_start, pencil_location):

    start_point = pencil_location

    total_length = 100

    current_length = 0
    while current_length < total_length:

        point_end = [start_point[0], start_point[1] + current_length]

        current_length += 10
        pencil_location = point_end

        draw_line(screen, point_start, point_end)
        screen.blit(pencil, pencil_location)
        pygame.display.flip()

    return point_start, point_end, pencil_location

def draw_line(screen, a, b):
    pygame.draw.line(screen, WHITE, a, b, 2)

while carry_on:
    screen.fill(DARKBLUE)
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carry_on = False  # Flag that we are done so we exit this loop


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        print("hello")
        point_start, point_end, pencil_location = draw_a_line(screen, point_start, pencil_location)

    screen.blit(pencil, pencil_location)
    draw_line(screen, point_start, point_end)

    pygame.display.flip()

    clock.tick(10)



pygame.quit()