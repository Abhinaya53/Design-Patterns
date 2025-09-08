from abc import ABC, abstractmethod

class ObserverInterface(ABC):
    @abstractmethod
    def update(self, stock_symbol: str, new_price: float, old_price: float) -> None: 
        pass