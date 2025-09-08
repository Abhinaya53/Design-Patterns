from abc import ABC, abstractmethod

class HandlerInterface(ABC):
    @abstractmethod
    def set_next_handler(self, handler):
        pass

    @abstractmethod
    def handle_query(self, query):
        pass