from abc import ABC, abstractmethod

class CheckboxInterface(ABC):
    @abstractmethod
    def render(self) -> None:
        pass