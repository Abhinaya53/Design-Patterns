from abc import ABC, abstractmethod
from ObserverInterface import ObserverInterface

class SubjectInterface(ABC):
    @abstractmethod
    def subscribe(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass