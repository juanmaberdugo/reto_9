from .point import Point
from .triangle import Triangle

class Isosceles(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        lengths = [edge.compute_length() for edge in self.edges]
        unique_lengths = set(lengths)
        if len(unique_lengths) > 2:
            print("Un triangulo isósceles debe tener al menos dos lados iguales.")