from Graphic import Graphic

class Dot(Graphic):
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def move(self,x: int, y: int) -> None:
        self._x += x
        self._y += y
    
    def draw(self) -> None:
        print(f"\nDrawing a Dot at position: ({self._x}, {self._y})")