from Dot import Dot

class Square(Dot):
    def __init__(self, x: int, y: int, length: int, breadth: int):
        super().__init__(x, y)
        self.__length = length
        self.__breadth = breadth

    def draw(self) -> None:
        super().draw()
        print(f"Shape: Square with length {self.__length} cm and breadth {self.__breadth} cm")