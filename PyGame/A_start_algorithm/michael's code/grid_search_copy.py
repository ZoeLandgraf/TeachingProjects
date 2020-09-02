import pygame
import numpy as np
import time
import queue

class Grid:
    # H o m e w o r k
    # write pseudo code for the entire search map algorithm - use grid_locations function!
    #
    # H I N T S
    # a. keep track of visited locations and the explorers.
    # b. there will be a loop involved (while True:), stop that while loop as well
    #   1. if you know how big the map is, you could use a for loop
    #       a. however, because we're searching for something, we should use a while loop as we
    #       dont know how big the map is.
    # c. there has to be a stopping condition (when do we stop searching?)

    def __init__(self, width, height):

        self.nbr_of_rows = 0
        self.nbr_of_cols = 0
        self.width = width
        self.height = height
        self.color = (200,200,200)
        self.square_dims = (20,20)
        self.square = pygame.Surface(self.square_dims)
        self.square.fill(self.color)
        self.empty_square = pygame.Surface(self.square_dims)
        self.empty_square.fill((150,150,150))
        self.locations, self.occupancy = self.create_empty_grid()




    def grid_locations(self):
        """
        Returns all grid locations as a list
        :return:
        """
        all_locs = []
        for i in range(self.nbr_of_cols):
            for j in range(self.nbr_of_rows):
                all_locs.append((i,j))
        return set(all_locs)

    def update_occupancy(self, occupied):
        """
        Updates the occupancy of the grid
        :param occupied:
        :return:
        """
        for i in range(self.nbr_of_cols):
            for j in range(self.nbr_of_rows):
                self.occupancy[i][j] = False
        for el in occupied:
            self.occupancy[el[0]][el[1]] = True

    def in_bounds(self, loc):
        """
        Tests whether or not a location is within the bounds of the grid
        :param loc:
        :return:
        """
        if loc[0] >= 0 and loc[0] < self.nbr_of_cols:
            if loc[1] >= 0 and loc[1] < self.nbr_of_rows:
                return True

        return False

    def create_empty_grid(self):
        """
        Creates the empty grid which is to be searched.
        :return:
        """

        gap_width = 3
        self.nbr_of_rows = self.height // (self.square_dims[1] + gap_width)
        self.nbr_of_cols = self.width // (self.square_dims[0] + gap_width)

        grid_matrix_location = np.zeros((self.nbr_of_cols, self.nbr_of_rows, 2))
        grid_matrix_occupancy = np.zeros((self.nbr_of_cols, self.nbr_of_rows)).astype(np.bool)

        start_x = 10
        start_y = 3
        for i in range(self.nbr_of_cols):
            for j in range(self.nbr_of_rows):
                pos_x = start_x + (self.square_dims[0] + gap_width) * i
                pos_y = start_y + (self.square_dims[1] + gap_width) * j
                grid_matrix_location[i][j][0] = pos_x
                grid_matrix_location[i][j][1] = pos_y

        #TODO

        return grid_matrix_location, grid_matrix_occupancy

    def get_neighbours(self, loc):
        """
        Finds the neighbours of a grid cell at location loc
        :param loc:
        :return:
        """
        x, y = loc
        neighbour_right = (x + 1, y)
        neighbour_left = (x - 1, y)
        neighbour_up = (x, y - 1)
        neighbour_down = (x, y + 1)

        neighbours = [neighbour_up, neighbour_down, neighbour_left, neighbour_right]

        valid_neighbours = []

        for neighbour in neighbours:
            if self.in_bounds(neighbour):
                valid_neighbours.append(neighbour)

        # valid_neighbours = [neighbour for neighbour in neighbours if self.in_bounds(neighbour)]

        return valid_neighbours

    def render_grid(self, display):
        """
        Renders the grid matrix to the display
        :param display:
        :return:
        """


        for i in range(self.nbr_of_cols):
            for j in range(self.nbr_of_rows):

                if self.occupancy[i][j]:
                    pos = self.locations[i][j]
                    display.blit(self.square, tuple(pos))
                else:
                    pos = self.locations[i][j]
                    display.blit(self.empty_square, tuple(pos))

                # pos_x = self.locations[i][j][0]
                # pos_y = self.locations[i][j][1]
                # display.blit(self.empty_square, (pos_x, pos_y))



    def render(self, display):
        """
        Renders the Grid
        :param display:
        :return:
        """
        self.render_grid(display)

class GameField:
    """
    This class holds the grid, start and end positions
    """
    def __init__(self, width, height):
        self._display_surf = pygame.display.set_mode((width, height), pygame.HWSURFACE)
        pygame.display.set_caption('Maze')

        self.grid = Grid(width, height)
        self.start_pos = None
        self.goal_pos = None
        self.frontier = queue.Queue()


    def set_start_and_goal(self, start_pos, goal_pos):
        self.start_pos = start_pos
        self.goal_pos = goal_pos



    def render(self):

        self._display_surf.fill((0,0,0))
        self.grid.render(self._display_surf)
        self.grid.update_occupancy(list(self.frontier.queue))

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


def search_map():
    clock = pygame.time.Clock()
    game = GameField(800, 600)
    game.set_start_and_goal((4, 4), (15, 12))
    empty_locations = game.grid.grid_locations()
    visited_locations = set()
    current_position = game.start_pos
    run = True
    print(len(empty_locations))


    while len(empty_locations) > 0 and run is True:
        valid_neighbours = game.grid.get_neighbours(current_position)
        for neighbour in valid_neighbours:
            if neighbour not in game.frontier.queue:
                if neighbour not in visited_locations:
                    game.frontier.put(neighbour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        visited_locations.add(current_position)

        current_position = game.frontier.get()

        empty_locations.remove(current_position)

        game.render()

        time.sleep(0.05)
        # while true:
        #   grid_locations()
        #   update_occupancy(current_explorer_positions)
        #   search? Square locations + 1x,y,-x,-y
        #

        #   if dot is found:
        #       break




def display_grid():
    game = GameField(800, 600)
    run = True
    game.set_start_and_goal((2, 2), (8, 20))
    while run:
        game.render()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.display.quit()
    pygame.quit()

def main():
    pygame.init()

    search_map()



main()