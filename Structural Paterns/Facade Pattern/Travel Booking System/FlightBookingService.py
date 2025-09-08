from BookingService import BookingService

class FlightBookingService(BookingService):
    def set_details(self, booking_config: dict):
        self.__source = booking_config["source"]
        self.__destination = booking_config["destination"]
        self.__amount = 5000
        
    def book(self):
        print(f"Flight booked from {self.__source} to {self.__destination}\n")
    
    def cancel(self):
        print(f"Flight booking from {self.__source} to {self.__destination} is cancelled\n")
    
    def generate_bill(self):
        print(f"Bill generated for Flight Booking Service:\nSource: {self.__source}\nDestination: {self.__destination}\nAmount: Rs. {self.__amount}\n")
        return self.__amount