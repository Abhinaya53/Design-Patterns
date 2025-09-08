from abc import ABC, abstractmethod

class StateInterface(ABC):
    @abstractmethod
    def can_write(self) -> bool:
        pass

    @abstractmethod
    def publish_process(self):
        pass