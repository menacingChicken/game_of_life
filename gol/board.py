class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash(self._x) ^ hash(self._y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.y or self.y != other.y

    def __repr__(self):
        return "(%i, %i)" % (self._x, self._y)


class Cell(object):
    def __init__(self, pos):
        self._pos = pos
        self._neighbors = set()
        self.alive = False

    @property
    def neighbors(self):
        return self._neighbors

    def add_neighbor(self, neighbor):
        self._neighbors.add(neighbor)

    @property
    def is_alive(self):
        return self.alive

    @property
    def is_dead(self):
        return not self.alive

    @property
    def neighbors_alive(self):
        return len([n for n in self._neighbors if n.is_alive])

    @property
    def neighbors_dead(self):
        return len([n for n in self._neighbors if n.is_dead])

    @property
    def pos(self):
        return self._pos

    def __repr__(self):
        return "<Cell: %r>" % self._pos

    def __eq__(self, other):
        return self._pos == other.pos

    def __ne__(self, other):
        return self._pos != other.pos

    def __hash__(self):
        return hash("cell") ^ hash(self._pos)


class Board(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height

        self._cells = None

        self._create_cells()

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def _create_cells(self):
        self._initialize_cells()

        def wrap(pnt):
            x, y = pnt.x, pnt.y

            if x < 0:
                x = self._width - 1
            elif x == self._width:
                x = 0
            if y < 0:
                y = self._height - 1
            elif y == self._height:
                y = 0

            return Point(x, y)

        for cell in self._cells.values():
            top_left = wrap(cell.pos + Point(-1, -1))
            top = wrap(cell.pos + Point(0, -1))
            top_right = wrap(cell.pos + Point(1, -1))
            right = wrap(cell.pos + Point(1, 0))
            bottom_right = wrap(cell.pos + Point(1, 1))
            bottom = wrap(cell.pos + Point(0, 1))
            bottom_left = wrap(cell.pos + Point(-1, 1))
            left = wrap(cell.pos + Point(-1, 0))

            for position in [top_left, top, top_right, right, bottom_right, bottom, bottom_left, left]:
                cell.add_neighbor(self.get(position.x, position.y))

    def _initialize_cells(self):
        self._cells = {}

        for y in range(self._height):
            for x in range(self._width):
                point = Point(x, y)
                self._cells[point] = Cell(point)

    def get(self, x, y):
        """

        :param x:
        :param y:
        :return: Cell
        :rtype: Cell
        """

        try:
            return self._cells[Point(x, y)]
        except KeyError:
            raise IndexError("no such point on board")

    def __iter__(self):
        for y in range(self._height):
            for x in range(self._width):
                yield self.get(x, y)
