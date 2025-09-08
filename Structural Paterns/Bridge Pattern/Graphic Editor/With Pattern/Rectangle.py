from Shape import Shape
from Renderer import Renderer

class Rectangle(Shape):
    def __init__(self, renderer: Renderer, x: int, y: int, length: int, breadth: int):
        super().__init__(renderer, x, y)
        self._length = length
        self._breadth = breadth
    
    def draw(self):
        self._renderer.render()
        print(f"Drawing Rectangle at ({self._x}, {self._y}) with length {self._length} and breadth {self._breadth}\n")