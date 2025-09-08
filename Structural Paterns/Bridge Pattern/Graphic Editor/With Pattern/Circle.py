from Shape import Shape
from Renderer import Renderer

class Circle(Shape):
    def __init__(self, renderer: Renderer, x: int, y: int, radius: int):
        super().__init__(renderer, x, y)
        self._radius = radius
    
    def draw(self):
        self._renderer.render()
        print(f"Drawing Circle at ({self._x}, {self._y}) with radius {self._radius}\n")