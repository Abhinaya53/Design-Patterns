from abc import ABC, abstractmethod

class HandlerInterface(ABC):
    @abstractmethod
    def process_payment(self, total_cost):
        pass