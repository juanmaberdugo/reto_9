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
