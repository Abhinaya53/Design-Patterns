from abc import ABC, abstractmethod

# Interface for Booking Service
class BookingService(ABC):
    @abstractmethod
    def set_details(self, booking_config: dict):
        pass
    
    @abstractmethod
    def book(self):
        pass

    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def generate_bill(self):
        pass