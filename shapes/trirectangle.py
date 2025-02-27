from .point import Point
from .triangle import Triangle

class TriRectangle(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        lengths = sorted([edge.compute_length() for edge in self.edges])
        a, b, c = lengths
        if abs(a**2 + b**2 - c**2) > 1e-9:
            print("Un triangulo rectángulo debe cumplir el teorema de Pitagoras.")