from abc import ABC, abstractmethod
from Renderer import Renderer

class Shape(ABC):
    def __init__(self, renderer: Renderer, x: int, y: int):
        self._renderer = renderer
        self._x = x
        self._y = y

    def move(self, dx: int, dy: int):
        self._x += dx
        self._y += dy

    def set_renderer(self, renderer: Renderer):
        self._renderer = renderer

    @abstractmethod
    def draw(self):
        pass