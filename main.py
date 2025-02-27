import shapes.rectangle as rectangle
import shapes.square as square
import shapes.point as point
import shapes.triangle as triangle
import shapes.trirectangle as trirectangle
from shapes import shapes 

def main():
    rect = rectangle.Rectangle(x=0, y=0, width=10, height=5)
    print(f"Area del rectángulo: {rect.compute_area()}")
    print(f"Perimetro del rectángulo: {rect.compute_perimeter()}")

    square1 = square.Square(x=0, y=0, side_length=10)
    print(f"Area del cuadrado: {square1.compute_area()}")
    print(f"Perimetro del cuadrado: {square1.compute_perimeter()}")

    triangle_vertices = [point.Point(0, 0), point.Point(4, 0), point.Point(0, 3)]
    triangle1 = triangle.Triangle(triangle_vertices)
    print(f"Area del triangulo: {triangle1.compute_area()}")
    print(f"Perimetro del triangulo: {triangle1.compute_perimeter()}")

    trirectangle_vertices = [point.Point(0, 0), point.Point(3, 0), point.Point(0, 4)]
    trirectangle1 = trirectangle.TriRectangle(trirectangle_vertices)
    print(f"Area del triangulo rectángulo: {trirectangle1.compute_area()}")
    print(f"Perimetro del triangulo rectangulo: {trirectangle1.compute_perimeter()}")

    triangle2 = shapes.Shape.define_shape(
        vertices=[(0, 0), (1, 0), (0.5, 1)],
        edges=[(0, 1), (1, 2), (2, 0)],
        inner_angles=[60, 60, 60],
        is_regular=True
    )

    print(triangle2.vertices)       
    print(triangle2.edges)          
    print(triangle2.inner_angles)   
    print(triangle2.is_regular)    

    area = triangle1.compute_area()
    print(f"Área del triángulo: {area}")


if __name__ == "__main__":
    main()