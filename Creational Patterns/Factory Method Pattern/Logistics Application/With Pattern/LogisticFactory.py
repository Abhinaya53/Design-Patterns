from abc import ABC, abstractmethod

class LogisticFactory(ABC):
    @abstractmethod
    def createTransport(self):
        pass