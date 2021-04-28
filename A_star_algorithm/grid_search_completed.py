import pygame
import numpy as np
import time
import queue

class Grid:

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.color = (200,200,200)
        self.square_dims = (20,20)
        self.square = pygame.Surface(self.square_dims)
        self.square.fill(self.color)
        self.empty_square = pygame.Surface(self.square_dims)
        self.empty_square.fill((150,150,150))
        self.current_square = pygame.Surface(self.square_dims)
        self.current_square.fill((255, 0, 0))
        self.goal_square = pygame.Surface(self.square_dims)
        self.goal_square.fill((0, 255, 0))
        self.path_square = pygame.Surface(self.square_dims)
        self.path_square.fill((100, 255, 0))
        self.obstacle_square = pygame.Surface(self.square_dims)
        self.obstacle_square.fill((10, 10, 10))
        self.locations, self.occupancy = self.create_empty_grid()
        self.obstacle_list = []

    def set_obstacle_list(self, o_list):
        self.obstacle_list = o_list

    def create_empty_grid(self):
        """

        :return:
        """
        gap_width = 3

        nbr_of_cols = self.height // (self.square_dims[1] + gap_width)
        nbr_of_rows = self.width // (self.square_dims[0] + gap_width)

        self.nbr_of_cols = nbr_of_cols
        self.nbr_of_rows = nbr_of_rows

        # this matrix holds the occupnacy of each square, initialized to zero
        grid_matrix_occupancy = np.zeros((nbr_of_rows, nbr_of_cols)).astype(np.bool)
        # this matrix holds the starting positions of each square
        grid_matrix_location = np.zeros((nbr_of_rows, nbr_of_cols, 2))

        start_x = 10
        start_y = 10
        for i in range(nbr_of_rows):
            for j in range(nbr_of_cols):
                pos_x = start_x + (self.square_dims[0] + gap_width) * i
                pos_y = start_y + (self.square_dims[1] + gap_width) * j
                grid_matrix_location[i][j][0] = pos_x
                grid_matrix_location[i][j][1] = pos_y


        return grid_matrix_location, grid_matrix_occupancy

    def in_bounds(self, loc):
        if loc[0] >= 0 and loc[0] < self.nbr_of_rows:
            if loc[1] >=0 and loc[1] < self.nbr_of_cols:
                return True
        return False

    def on_obstacle(self, loc):

        if loc in self.obstacle_list:
            return True

        return False


    def get_neighbours(self, loc):

        i, j = loc
        # for now don't include diagonal neighbours
        up = (i,j - 1)
        down = (i, j + 1)
        right = (i + 1,j)
        left = (i - 1, j)

        neighbours = [up, down, right, left]
        valid_neighbours = [el for el in neighbours if self.in_bounds(el) and not self.on_obstacle(el)]

        return valid_neighbours

    def update_occupancy(self, occupied):
        for i in range(self.nbr_of_rows):
            for j in range(self.nbr_of_cols):
                self.occupancy[i][j] = False
        for el in occupied:
            self.occupancy[el[0]][el[1]] = True

    def all_locations(self):

        all_locs = []
        for i in range(self.nbr_of_rows):
            for j in range(self.nbr_of_cols):
                all_locs.append((i,j))
        return set(all_locs)


    def render_grid(self, display, current_pos, found_goal, path_positions):
        rows, cols = self.occupancy.shape[0], self.occupancy.shape[1]

        for i in range(rows):
            for j in range(cols):

                if path_positions is not None:
                    if (i,j) in path_positions:
                        pos = self.locations[i][j]
                        display.blit(self.path_square, tuple(pos))
                        continue

                if found_goal is not None:
                    if found_goal == (i,j):
                        pos = self.locations[i][j]
                        display.blit(self.goal_square, tuple(pos))
                        continue

                # if current_pos == (i,j):
                #     pos = self.locations[i][j]
                #     display.blit(self.current_square, tuple(pos))
                #     continue

                if (i,j) in self.obstacle_list:
                    pos = self.locations[i][j]
                    display.blit(self.obstacle_square, tuple(pos))

                elif self.occupancy[i][j]:
                    pos = self.locations[i][j]
                    display.blit(self.square, tuple(pos))
                else:
                    pos = self.locations[i][j]
                    display.blit(self.empty_square, tuple(pos))



    def render(self, display, current_pos, found_goal, path_positions):

        self.render_grid(display,
                         current_pos,
                         found_goal,
                         path_positions)


class GameField:

    def __init__(self, width, height):
        self._display_surf = pygame.display.set_mode((width, height), pygame.HWSURFACE)
        pygame.display.set_caption('Maze')

        self.found_goal = None
        self.path_positions = None
        self.grid = Grid(width, height)
        self.start_pos = None
        self.goal_pos = None
        self.frontier = queue.Queue()
        self.current = self.start_pos


    def set_start_and_goal(self, start_pos, goal_pos):
        self.start_pos = start_pos
        self.goal_pos = goal_pos



    def render(self):

        self._display_surf.fill((0,0,0))
        self.grid.update_occupancy(list(self.frontier.queue))
        self.grid.render(self._display_surf,
                         self.current,
                         self.found_goal,
                         self.path_positions)



        if self.start_pos is not None and self.goal_pos is not None:
            location_start = self.grid.locations[self.start_pos[0]][self.start_pos[1]]
            loc_x = location_start[0] + self.grid.square_dims[0]//2
            loc_y = location_start[1] + self.grid.square_dims[1]//2
            pygame.draw.circle(self._display_surf, (0,250,0), (int(loc_x),int(loc_y)), 5)
            location_goal = self.grid.locations[self.goal_pos[0]][self.goal_pos[1]]
            loc_g_x = location_goal[0] + self.grid.square_dims[0] // 2
            loc_g_y = location_goal[1] + self.grid.square_dims[1] // 2

            pygame.draw.circle(self._display_surf, (250,150,0), (int(loc_g_x), int(loc_g_y)), 5)
        pygame.display.update()



def render_empty_grid(gf):
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        gf.render()

def search_map(gf):
    clock = pygame.time.Clock()
    unseen = gf.grid.all_locations()
    visited = set()

    run = True
    count = 0
    current = gf.start_pos
    came_from = {}
    came_from[gf.start_pos] = None

    while len(unseen) != 0 and count < 5000 and run:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        neighbours = gf.grid.get_neighbours(current)
        visited.add(current)

        if current in unseen:

            unseen.remove(current)
        else:

            print(current)
            print("WARNING")

        for el in neighbours:
            if el not in visited:
                if el not in gf.frontier.queue:
                    gf.frontier.put(el)
                    came_from[el] = current

        gf.render()

        if gf.frontier.empty():
            break


        next = gf.frontier.get()


        if gf.goal_pos in gf.frontier.queue:
            gf.found_goal = gf.goal_pos
            break


        gf.current = next
        current = next

        count += 1

        clock.tick(100)
        time.sleep(0.05)

    # vis path
    pos = gf.goal_pos
    run = True
    gf.path_positions = [gf.goal_pos]

    # import pdb;pdb.set_trace()
    time.sleep(0.40)

    while pos is not None and run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pos = came_from[pos]
        gf.path_positions.append(pos)
        gf.render()
        clock.tick(100)
        time.sleep(0.2)

def main():

    pygame.init()

    gf = GameField(640,480)
    gf.set_start_and_goal((4,4), (8,8))

    obstacle_list = [(3,3), (4,3), (5,3), (6,3), (7,3), (7,4), (7,5), (7,6), (7,7), (7,8),
                     (7,9), (8,9), (8,10), (4,6),(3,6), (3,7)]
    gf.grid.set_obstacle_list(obstacle_list)

    search_map(gf)

    pygame.display.quit()
    pygame.quit()


main()