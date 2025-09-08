from abc import ABC, abstractmethod

# Implementation Interface
class Renderer(ABC):
    @abstractmethod
    def render(self):
        pass