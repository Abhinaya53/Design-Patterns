from abc import ABC, abstractmethod
from ObserverInterface import ObserverInterface

class SubjectInterface(ABC):
    @abstractmethod
    def register_observer(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: ObserverInterface) -> None:
        pass

    @abstractmethod
    def notify_observers(self, stock_symbol: str, new_price: float, old_price: float) -> None:
        pass