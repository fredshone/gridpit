import random


class Agent:

    def __init__(self, grid, start, colour):
        self.searching = True
        self.grid = grid
        self.loc = start
        self.neighbours = []
        self.colour = colour

    def get_neighbours(self):
        self.neighbours = []
        for dy in range(-1, 2):
            y = self.loc.y + dy
            if 0 <= y < self.grid.height:
                for dx in range(-1, 2):
                    x = self.loc.x + dx
                    if 0 <= x < self.grid.width:
                        if not (dx == dy == 0):
                            if not self.grid.zones[y][x].blocker:
                                self.neighbours.append(self.grid.zones[y][x])

    def select_neighbour(self):
        return random.choice(self.neighbours)

    def move(self):
        self.get_neighbours()
        self.loc = self.select_neighbour()
        self.loc.h = self.colour
        if self.loc == self.grid.finish:
            self.searching = False
        self.grid.update()