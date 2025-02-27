from .point import Point
from .triangle import Triangle

class Scalene(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        lengths = [edge.compute_length() for edge in self.edges]
        unique_lengths = set(lengths)
        if len(unique_lengths) != 3:
            print("Un triangulo escaleno debe tener todos los lados de diferente longitud.")