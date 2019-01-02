import random
import numpy as np


class Loc:

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def equals(self, other):
        if self.y == other.y and self.x == other.x:
            return True
        return False

    def within(self, others):
        for other in others:
            if self.y == other.loc.y and self.x == other.loc.x:
                return True
        return False

    def search(self, others):
        for other in others:
            if self.equals(other.loc):
                return other
        print('not found')
        return None


class Node:

    def __init__(self, y, x):
        self.loc = Loc(y, x)
        self.gscore = np.inf
        self.fscore = np.Inf
        self.came_from = None


def dist(loc1, loc2):
    return np.sqrt(((loc1.y - loc2.y) ** 2) + ((loc1.x - loc2.x) ** 2))


def reconstruct_path(came_from, current):
    path = []
    return path


class Agent:

    def __init__(self, grid, start, goal, colour):
        self.searching = True
        self.grid = grid
        self.scores = []
        self.neighbours = []
        self.colour = colour
        self.start = start
        self.goal = goal
        self.loc = None
        self.closed_set = []
        self.open_set = []

        self.nodes = []
        for y in range(grid.height):
            row = []
            for x in range(grid.width):
                row.append(Node(y, x))
            self.nodes.append(row)

        print('starting:')
        self.loc = self.start.loc
        node = self.nodes[self.loc.y][self.loc.x]
        node.gscore = 0
        node.fscore = dist(self.loc, self.goal.loc)
        self.open_set.append(node)

    def search(self):

        self.grid.draw(self.grid.canvas())
        iteration = 0

        while self.searching:
            print('searching iteration {}:'.format(iteration))

            min_n = 0
            current = self.open_set[min_n]
            for n, node in enumerate(self.open_set):
                if node.fscore < current.fscore:
                    min_n = n
                    current = node

            self.loc = current.loc

            self.grid.zones[current.loc.y][current.loc.x].h = (0.8, .2, 0.2, 0.6)
            self.grid.draw(self.grid.canvas())

            if current.loc.equals(self.goal.loc):
                print('DONE')
                self.searching = False
                return self.reconstruct_path(current)

            del self.open_set[min_n]
            self.closed_set.append(current)

            for neighbour in self.get_neighbours():
                node = self.nodes[neighbour.loc.y][neighbour.loc.x]

                if node.loc.within(self.closed_set):
                    continue

                self.grid.zones[node.loc.y][node.loc.x].h = (0.5, 1, 0.2, 0.3)

                tentative = current.gscore + dist(current.loc, neighbour.loc)

                if not node.loc.within(self.open_set):
                    self.open_set += [node]
                elif tentative >= node.gscore:
                    continue

                self.grid.zones[node.loc.y][node.loc.x].h = (0.5, 1, 0.2, 0.6)

                node.came_from = current
                node.gscore = tentative
                node.fscore = tentative + dist(node.loc, self.goal.loc)

                self.grid.draw(self.grid.canvas())

            iteration += 1

    def get_neighbours(self):
        neighbours = []
        for dy in range(-1, 2):
            y = self.loc.y + dy
            if 0 <= y < self.grid.height:
                for dx in range(-1, 2):
                    x = self.loc.x + dx
                    if 0 <= x < self.grid.width:
                        if not (dx == dy == 0):
                            if not self.grid.zones[y][x].blocker:
                                neighbours.append(self.grid.zones[y][x])
        return neighbours

    def reconstruct_path(self, current):
        total_path = [current]
        while current:
            self.grid.zones[current.loc.y][current.loc.x].h = (0.5, 0.5, 1, 0.6)
            self.grid.draw(self.grid.canvas())
            total_path.append(current.came_from)
            current = current.came_from
        self.grid.draw(self.grid.canvas())
        return total_path

    def select_neighbour(self):
        return random.choice(self.neighbours)

    def move(self):
        self.get_neighbours()
        self.loc = self.select_neighbour()
        self.loc.h = self.colour
        if self.loc == self.grid.finish:
            self.searching = False
        self.grid.draw(self.grid.canvas())