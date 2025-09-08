from typing import List
from Graphic import Graphic

class CompoundGraphic(Graphic):
    def __init__(self):
        self.__components: List[Graphic] = []
    
    def add_component(self, component: Graphic):
        self.__components.append(component)

    def move(self, x, y):
        for component in self.__components:
            component.move(x, y)
    
    def draw(self):
        for component in self.__components:
            component.draw()