from abc import ABC, abstractmethod
from HideableUIComponent import HideableUIComponent

class MediatorInterface(ABC):
    @abstractmethod
    def show_component(self, component: HideableUIComponent):
        pass

    @abstractmethod
    def hide_component(self, component: HideableUIComponent):
        pass

    @abstractmethod
    def checkbox_checked(self):
        pass

    @abstractmethod
    def checkbox_unchecked(self):
        pass