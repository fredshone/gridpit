import numpy as np
import matplotlib.pyplot as plt
import random
from astar import Agent as Astar


class Loc:

    def __init__(self, y, x):
        self.y = y
        self.x = x


class Zone:

    def __init__(self, y, x, blockers):
        self.loc = Loc(y, x)
        self.h = (0, 0, 0)
        self.blocker = False
        if blockers:
            if random.randrange(100) < blockers:
                self.blocker = True


class Grid:

    def __init__(self, height, width, blockers=False):
        self.height = height
        self.width = width
        self.zones = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(Zone(y, x, blockers))
            self.zones.append(row)
        self.start = self.zones[0][0]
        self.start.blocker = False
        self.finish = self.zones[height - 1][width - 1]
        self.finish.blocker = False

        self.set_blank()
        self.fig, ax = plt.subplots(1, 1)
        self.im = ax.imshow(self.canvas())

    def wall(self):
        x = int(self.width / 2)
        for y in range(self.height - 5):
            self.zones[y][x].blocker = True


    def distance(self, loc):
        dist = np.sqrt(((loc.y - self.finish.loc.y) ** 2) + ((loc.x - self.finish.loc.x) ** 2))
        dist /= np.sqrt((self.height ** 2) + (self.width ** 2))
        return dist

    def set_background(self):
        for y in range(self.height):
            for x in range(self.width):
                zone = self.zones[y][x]
                zone.h = (self.distance(zone.loc) * 1, .5, .5, 1)
        self.start.h = (1, 0, 0, 1)
        self.finish.h = (0, 1, 0, 1)

    def set_blank(self):
        for y in range(self.height):
            for x in range(self.width):
                self.zones[y][x].h = (1, 1, 1, 1)
        self.start.h = (1, 0, 0, 1)
        self.finish.h = (0, 1, 0, 1)

    def canvas(self):
        canvas = np.zeros((self.height, self.width, 4))
        for y in range(self.height):
            for x in range(self.width):
                zone = self.zones[y][x]
                canvas[y, x] = zone.h
                if self.zones[y][x].blocker:
                    canvas[y, x] = (0, 0, 0, 1)
        return canvas

    def draw(self, canvas):
        self.im.set_data(canvas)
        self.fig.canvas.draw_idle()
        plt.pause(0.000001)

    def show(self, canvas):
        self.im.set_data(canvas)
        # self.fig.canvas.draw_idle()
        # plt.pause(.001)


grid = Grid(25, 25)
grid.wall()
astar = Astar(grid, grid.start, grid.finish, (0, 0, 0, 1))
astar.search()

user = input('exit? - enter any key')









# agents = []
# num_agent = 10
# for i in range(num_agent):
#     agents.append(Agent(grid, grid.start, (0, 0, 1, 1)))
#     agents.append(Agent(grid, grid.finish, (1, 0, 0, 1)))
#
# fig, ax = plt.subplots(1, 1)
# im = ax.imshow(grid.update())
# plt.pause(.1)
# while agents[0].searching:
#     grid.score()
#     for i in range(len(agents)):
#         agents[i].move()
#     image = grid.update()
#     im.set_data(image)
#     fig.canvas.draw_idle()
#     plt.pause(.01)


