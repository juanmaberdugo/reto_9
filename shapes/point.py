class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, y):
        self._y = y

    def compute_distance(self, point: "Point") -> float:
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
