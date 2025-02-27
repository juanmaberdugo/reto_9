from .triangle import Triangle
from .point import Point

class Equilateral(Triangle):
    def __init__(self, vertices: list[Point]):
        super().__init__(vertices)
        first_length = self.edges[0].compute_length()
        for edge in self.edges:
            if abs(edge.compute_length() - first_length) > 1e-9:
                print("Todos los lados de un triangulo equilatero deben ser iguales.")
        self.is_regular = True
