import queue
import pygame
import numpy as np
# HOMEWORK
#


class GridSearch:

    def __init__(self, barriers, game_dims, nbr_of_rows, nbr_of_columns):

        self.barriers = barriers
        self.game_dims = game_dims
        self.nbr_of_rows = nbr_of_rows
        self.nbr_of_columns = nbr_of_columns


    def in_grid_bounds(self, pos):
        if not (np.array(pos) > 1).all():
            return False
        return True

    def search_n_follow(self, goal_pos, start_pos):
        """
                Finds the path to the goal position and generates the
                list of steps to reach it
                :param goal_pos:
                :param start_pos:
                :return:
                """

        if not self.in_grid_bounds(goal_pos):
            return []

        if goal_pos in self.barriers:
            return []

        empty_locations = self.grid_locations()
        visited_locations = set()
        current = start_pos
        came_from = dict()
        came_from[start_pos] = None
        run = True
        frontier = queue.PriorityQueue()

        while len(empty_locations) > 0 and run is True:
            valid_neighbours = self.get_neighbours(current)
            for neighbour in valid_neighbours:
                if neighbour not in visited_locations:
                    if neighbour not in frontier.queue:
                        if neighbour not in self.barriers:
                            distance = self.heuristic(neighbour, goal_pos=goal_pos)
                            frontier.put((distance, neighbour))
                            came_from[neighbour] = current

            visited_locations.add(current)

            current = frontier.get()[1]

            if current in empty_locations:
                empty_locations.remove(current)

            if current == goal_pos:
                run = False

            for t in frontier.queue:
                if goal_pos == t[1]:
                    run = False

        # ------------------------
        run = True
        path_positions = [goal_pos]
        pos = goal_pos

        while pos is not None and run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pos = came_from[pos]
            if pos is not None:
                path_positions.append(pos)

        # need to reverse path
        path_positions.reverse()
        return path_positions


    def grid_locations(self):
        """
        Returns all grid locations as a list
        :return:
        """
        all_locs = []
        for i in range(self.nbr_of_columns):
            for j in range(self.nbr_of_rows):
                all_locs.append((i,j))
        return set(all_locs)

    def in_bounds(self, loc):
        """
        Tests whether or not a location is within the bounds of the grid
        :param loc:
        :return:
        """
        if loc[0] >= 0 and loc[0] < self.nbr_of_columns:
            if loc[1] >= 0 and loc[1] < self.nbr_of_rows:
                return True

        return False

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

        return valid_neighbours

    def heuristic(self, squarepos, goal_pos):
        x,y = squarepos
        x_goal = goal_pos[0]
        y_goal = goal_pos[1]
        distance = abs(y_goal-y) + abs(x_goal-x)
        return distance




