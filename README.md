# reto_9

- Add the @property decorator into the package Shape, so all the protected data could be accessed this way.

Para este caso en la clase shape se tomaron los atributos vertices, edges e inner_angles y se cambiaron a tipo protegido luego usando el decorador @property se crearon metodos para acceder a la informacion de estos atributos tambien se uso el decorador @.setter para poder cambiar el valor de estos.

```python
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
```

- Add @classmethod decorator to Shape, in order to change define and change the type of shape of each class.

Para este, se creo la clase define_shape() con el decorador @classmethod para que esta funcion pueda crear una instancia de shape sin instanciarla directamente.

```python
@classmethod
def define_shape(cls, vertices, edges, inner_angles, is_regular=False):
    shape = cls(is_regular)
    shape.vertices = vertices
    shape.edges = edges
    shape.inner_angles = inner_angles
    return shape
```

- Add a custom decorator in Shape co show the computation time of at least one operation. e.g: compute_area.

Se generar un decorador personalizado en la clase Triangle para que este generador calcule el tiempo de ejecucion al usar el metodo compute_area() y compute_perimeter().

```python
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
```
