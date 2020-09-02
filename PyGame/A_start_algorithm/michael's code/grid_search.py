import pygame
import numpy as np
import time

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
        self.locations, self.occupancy = self.create_empty_grid()
        self.nbr_of_rows = 0
        self.nbr_of_cols = 0

    def grid_locations(self):
        """
        Returns all grid locations as a list
        :return:
        """
        all_locs = []
        for i in range(self.nbr_of_rows):
            for j in range(self.nbr_of_cols):
                all_locs.append((i,j))
        return set(all_locs)

    def update_occupancy(self, occupied):
        """
        Updates the occupancy of the grid
        :param occupied:
        :return:
        """
        for i in range(self.nbr_of_rows):
            for j in range(self.nbr_of_cols):
                self.occupancy[i][j] = False
        for el in occupied:
            self.occupancy[el[0]][el[1]] = True

    def in_bounds(self, loc):
        """
        Tests whether or not a location is within the bounds of the grid
        :param loc:
        :return:
        """
        if loc[0] >= 0 and loc[0] < self.nbr_of_rows:
            if loc[1] >=0 and loc[1] < self.nbr_of_cols:
                return True

        return False

    def create_empty_grid(self):
        """
        Creates the empty grid which is to be searched.
        :return:
        """

        #TODO
        grid_matrix_location = None
        grid_matrix_occupancy = None

        return grid_matrix_location, grid_matrix_occupancy

    def get_neighbours(self, loc):
        """
        Finds the neighbours of a grid cell at location loc
        :param loc:
        :return:
        """
        #TODO
        valid_neighbours = []
        return valid_neighbours

    def render_grid(self, display):
        """
        Renders the grid matrix to the display
        :param display:
        :return:
        """
        #TODO
        pass

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
        self.frontier = set()


    def set_start_and_goal(self, start_pos, goal_pos):
        self.start_pos = start_pos
        self.goal_pos = goal_pos



    def render(self):

        self._display_surf.fill((0,0,0))
        self.grid.render(self._display_surf)
        self.grid.update_occupancy(self.frontier)


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
    #TODO

def main():

    pygame.init()

    #TODO

    pygame.display.quit()
    pygame.quit()


main()