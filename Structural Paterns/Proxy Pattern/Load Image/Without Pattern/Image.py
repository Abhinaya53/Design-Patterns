from abc import ABC, abstractmethod

# Interface
class Image(ABC):
    @abstractmethod
    def display(self) -> None:
        pass