from abc import ABC, abstractmethod

class TransportInterface(ABC):
    @abstractmethod
    def deliver(self):
        pass 