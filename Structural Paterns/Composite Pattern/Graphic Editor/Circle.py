from Dot import Dot

class Circle(Dot):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.__radius = radius

    def draw(self) -> None:
        super().draw()
        print(f"Shape: Circle with radius {self.__radius} cm")