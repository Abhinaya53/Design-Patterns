from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def register_flight(self, flight):
        pass

    @abstractmethod
    def handle_takeoff_request(self, flight):
        pass

    @abstractmethod
    def handle_landing_request(self, flight):
        pass
    
    @abstractmethod
    def notify_takeoff_complete(self, flight):
        pass

    @abstractmethod
    def notify_landing_complete(self, flight):
        pass
    