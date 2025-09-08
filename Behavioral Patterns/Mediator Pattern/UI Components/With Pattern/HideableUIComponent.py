from abc import ABC, abstractmethod

class HideableUIComponent(ABC):
    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass