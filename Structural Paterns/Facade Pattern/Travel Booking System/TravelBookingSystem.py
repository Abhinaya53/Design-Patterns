from BookingService import BookingService
from CarRentalService import CarRentalService
from FlightBookingService import FlightBookingService
from HotelBookingService import HotelBookingService
from PaymentService import PaymentService
from typing import List

# Facade
class TravelBookingSystem:
    def __init__(self):
        self.__booking_services: List[BookingService] = []
        self.__booking_services.append(FlightBookingService())
        self.__booking_services.append(HotelBookingService())
        self.__booking_services.append(CarRentalService())
        self._payment_service = PaymentService()

    def book_full_travel_package(self, booking_config: dict):
        for service in self.__booking_services:
            service.set_details(booking_config)
            service.book()

    def cancel_full_travel_package(self):
        for service in self.__booking_services:
            service.cancel()

    def process_full_payment(self):
        total_amount = 0
        for service in self.__booking_services:
            total_amount += service.generate_bill()
        
        print(f"Grand Total: Rs. {total_amount}")
        self._payment_service.process_payment(total_amount)