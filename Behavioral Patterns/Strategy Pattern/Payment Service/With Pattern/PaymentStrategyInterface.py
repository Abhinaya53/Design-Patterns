from abc import ABC, abstractmethod

class PaymentStrategyInterface(ABC):            #Strategy
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass