from abc import ABC, abstractmethod

class StateInterface(ABC):
    @abstractmethod
    def press_play(self):
        pass

    @abstractmethod
    def press_pause(self):
        pass

    @abstractmethod
    def press_stop(self):
        pass