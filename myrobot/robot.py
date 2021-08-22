from re import compile, X

class Robot():
    """Simulate a robot moving on a 5x5 grid"""

    def __init__(self):
        self._x = 0
        self._y = 0
        self._f = None
    
    def init_place(self):
        """if the first command to the robot is a PLACE command"""
        if self._f == None:
            return False
        else:
            return True

    def parse(self, line):
        """Parse one command line and return valid components. An exception is raised if the line does not correspond to a valid command
        string.
        """

        if len(line) == 0:
            raise ValueError('InvalidCommand')

        tokens = line.strip().split()
        # print ("tokens=", tokens)

        cmd = tokens[0]
        if cmd not in {'MOVE', 'LEFT', 'RIGHT', 'REPORT', 'PLACE'}:
            raise ValueError('InvalidCommand')

        coords = None
        if cmd == 'PLACE':
            if len(tokens) < 2:
                 raise ValueError('InvalidCommand')

            PATTERN = compile(
                r"""
                    (?P<x>\d+),                  # x coord
                    (?P<y>\d+),                  # y coord
                    (?P<f>NORTH|EAST|SOUTH|WEST) # facing
                    """, X
            )

            valid = PATTERN.search(tokens[1])
            # print ("valid=", valid)
            if not valid:
                raise ValueError('InvalidCommand')

            coords = dict(
                x=int(valid['x']),  # regexp ensures the str is a digit
                y=int(valid['y']),
                f=valid['f'],
            )
        # print ("return=", cmd, coords)
        return cmd, coords

    def get_position(self):
        return dict(x=self._x, y=self._y, f=self._f)
    
    def valid_position(self, c):
        """verify the position"""
        X_RANGE = {0, 1, 2, 3, 4}
        Y_RANGE = {0, 1, 2, 3, 4}
        F_RANGE = {'NORTH', 'EAST', 'SOUTH', 'WEST'}

        if c['x'] in X_RANGE and c['y'] in Y_RANGE and c['f'] in F_RANGE:
            return True
        else:
            return False

    def update_position(self, c):
        """set position"""
        self._x = c['x']
        self._y = c['y']
        self._f = c['f']

    def move(self):
        """Move the robot one unit in the direction it is currently facing"""
        c = self.get_position()

        f = c['f']
        if f == 'NORTH':
            c['y'] += 1
        elif f == 'EAST':
            c['x'] += 1
        elif f == 'SOUTH':
            c['y'] -= 1
        elif f == 'WEST':
            c['x'] -= 1

        if self.valid_position(c):
            self.update_position(c)
        else:
            raise ValueError('InvalidPosition')
    
    def __str__(self):
        return "{},{},{}".format(self._x, self._y, self._f)
    
    def report(self):
        print ("{},{},{}".format(self._x, self._y, self._f))
    
    def turn(self, cmd):
        COMPASS = {
            'NORTH': {
                'left': 'WEST',
                'right': 'EAST'
            },
            'WEST': {
                'left': 'SOUTH',
                'right': 'NORTH'
            },
            'SOUTH': {
                'left': 'EAST',
                'right': 'WEST'
            },
            'EAST': {
                'left': 'NORTH',
                'right': 'SOUTH'
            },
        }

        c = self.get_position()
        f = c['f']

        if cmd == 'LEFT':    
            c['f'] = COMPASS[f]['left']
        else:
            c['f'] = COMPASS[f]['right']

        self.update_position(c)