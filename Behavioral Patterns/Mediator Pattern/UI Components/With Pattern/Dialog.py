from MediatorInterface import MediatorInterface
from HideableUIComponent import HideableUIComponent

class Dialog(MediatorInterface):
    def __init__(self):
        self.__components = []

    def add_component(self, component: HideableUIComponent):
        if component not in self.__components:
            self.__components.append(component)
    
    def checkbox_checked(self):
        for component in self.__components:
            self.show_component(component)
    
    def checkbox_unchecked(self):
        for component in self.__components:
            self.hide_component(component)
    
    def show_component(self, component: HideableUIComponent):
        component.enable()
    
    def hide_component(self, component: HideableUIComponent):
        component.disable()
    
