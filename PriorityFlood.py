from heapq import *


class PriorityFlood:
    def __init__(self, dem):
        self.dem = dem
        self.size = (len(self.dem), len(self.dem[0]))

        # empty priority queue
        self.open = []
        # empty plain queue
        self.pit = []
        # keeps track of what locations have been visited
        self.closed = [[False for x in range(self.size[0])] for y in range(self.size[1])]

        self.moves = [
            (1, 0),
            (1, -1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, 1),
        ]

    def flood(self):

        # PUSH ALL EDGES OF THE DEM TO THE PRIORITY QUEUE AND CLOSE THEIR POSITIONS

        # top / bottom
        for j in range(0, self.size[1]):
            heappush(self.open, [self.dem[0][j], (0, j)])
            heappush(self.open, [self.dem[self.size[0] - 1][j], (self.size[0] - 1, j)])
            self.closed[self.size[0] - 1][j] = True
            self.closed[0][j] = True
        # left / right
        for j in range(1, self.size[1] - 1):
            heappush(self.open, [self.dem[j][0], (j, 0)])
            heappush(self.open, [self.dem[j][self.size[1] - 1], (j, self.size[1] - 1)])
            self.closed[j][self.size[1] - 1] = True
            self.closed[j][0] = True

        # BEGIN PROCESSING THE VALUES IN THE QUEUE(S), STARTING WITH THE LOWEST VALUE

        while self.open or self.pit:

            # pops a value from the plain queue if it can
            if self.pit:
                loc = self.pit.pop(0)[1]
            # if it is empty, pops a value from the priority queue
            else:
                loc = heappop(self.open)[1]

            # for every neighbor of the location...
            for i in range(len(self.moves)):
                neighbor = (loc[0] + self.moves[i][0], loc[1] + self.moves[i][1])
                # if the neighbor is in bounds...
                if self.is_legal_move(neighbor):
                    # and has not already been closed...
                    if not self.get_closed(neighbor):
                        # close the location of the neighbor
                        self.closed[neighbor[0]][neighbor[1]] = True

                        # if it is lower than the location which was popped...
                        if self.dem[neighbor[0]][neighbor[1]] <= self.dem[loc[0]][loc[1]]:
                            # raise it to the height of that location
                            self.dem[neighbor[0]][neighbor[1]] = self.dem[loc[0]][loc[1]]
                            # and append it to the plain queue
                            self.pit.append([self.dem[neighbor[0]][neighbor[1]], neighbor])
                        # otherwise, push it to the priority queue
                        else:
                            heappush(self.open, [self.dem[neighbor[0]][neighbor[1]], neighbor])

    def is_legal_move(self, loc):
        legal = True
        if 0 > loc[0] or self.size[0] - 1 < loc[0]:
            legal = False
        if 0 > loc[1] or self.size[1] - 1 < loc[1]:
            legal = False

        return legal

    def get_closed(self, location):
        return self.closed[location[0]][location[1]]

    def get_dem(self):
        return self.dem
