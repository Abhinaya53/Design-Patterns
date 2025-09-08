from abc import ABC, abstractmethod

# Interface
class Graphic(ABC):
    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass