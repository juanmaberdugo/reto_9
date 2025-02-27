from .point import Point

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self._start_point = start_point
        self._end_point = end_point
    
    @property
    def start_point(self):
        return self._start_point
    
    @start_point.setter
    def start_point(self, start_point):
        self._start_point = start_point

    @property
    def end_point(self):
        return self._end_point
    
    @end_point.setter
    def end_point(self, end_point):
        self._end_point = end_point

    def compute_length(self) -> float:
        return self.start_point.compute_distance(self.end_point)