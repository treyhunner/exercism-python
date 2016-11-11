NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)


class Robot:

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x, self.y = x, y

    @property
    def coordinates(self):
        return self.x, self.y

    def advance(self):
        x, y = self.bearing
        self.x += x
        self.y += y

    def turn_left(self):
        x, y = self.bearing
        self.bearing = -y, x

    def turn_right(self):
        x, y = self.bearing
        self.bearing = y, -x

    def simulate(self, steps):
        actions = {
            'R': self.turn_right,
            'L': self.turn_left,
            'A': self.advance,
        }
        for step in steps:
            actions[step]()
