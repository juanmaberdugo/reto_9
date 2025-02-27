from .point import Point
from .shapes import Shape
from .line import Line
import time

class Triangle(Shape):
    def __init__(self, vertices: list[Point]):
        super().__init__(is_regular=False)
        if len(vertices) != 3:
            print("Un triángulo debe tener exactamente 3 vértices.")
        self.vertices = vertices
        self.edges = []
        self._build_edges()

    def _build_edges(self):
        first_edge = Line(self.vertices[0], self.vertices[1])
        second_edge = Line(self.vertices[1], self.vertices[2])
        third_edge = Line(self.vertices[2], self.vertices[0])
        self.edges.append(first_edge)
        self.edges.append(second_edge)
        self.edges.append(third_edge)

    def timing_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Tiempo de ejecucion para {func.__name__}: {end_time - start_time:.6f} segundos")
            return result
        return wrapper

    @timing_decorator
    def compute_perimeter(self) -> float:
        total_length = 0
        for edge in self.edges:
            total_length += edge.compute_length()
        return total_length

    @timing_decorator
    def compute_area(self) -> float:
        a = self.edges[0].compute_length()
        b = self.edges[1].compute_length()
        c = self.edges[2].compute_length()
        s = self.compute_perimeter() / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return area
