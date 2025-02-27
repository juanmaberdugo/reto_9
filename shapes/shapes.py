import time

class Shape:
    def __init__(self, is_regular: bool = False):
        self.is_regular = is_regular
        self._vertices = []
        self._edges = []
        self._inner_angles = [] 

    @property
    def vertices(self):
        return self._vertices
    
    @vertices.setter
    def vertices(self, vertices):
        self._vertices = vertices

    @property
    def edges(self):
        return self._edges
    
    @edges.setter
    def edges(self, edges):
        self._edges = edges

    @property
    def inner_angles(self):
        return self._inner_angles
    
    @inner_angles.setter
    def inner_angles(self, inner_angles):
        self._inner_angles = inner_angles

    def timing_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Execution time for {func.__name__}: {end_time - start_time:.6f} seconds")
            return result
        return wrapper

    @timing_decorator
    def compute_area(self):
        ...

    @timing_decorator
    def compute_perimeter(self):
        ...

    @classmethod
    def define_shape(cls, vertices, edges, inner_angles, is_regular=False):
        shape = cls(is_regular)
        shape.vertices = vertices
        shape.edges = edges
        shape.inner_angles = inner_angles
        return shape