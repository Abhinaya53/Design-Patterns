from abc import ABC, abstractmethod

class ButtonInterface(ABC):
    @abstractmethod
    def render(self) -> None:
        pass