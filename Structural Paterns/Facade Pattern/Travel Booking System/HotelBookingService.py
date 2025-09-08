from BookingService import BookingService

class HotelBookingService(BookingService):
    def set_details(self, booking_config: dict):
        self.__place = booking_config["destination"]
        self.__number_of_nights = booking_config["number_of_nights"]
        self.__rate_per_night = 6000
        
    def book(self):
        print(f"Hotel booked in {self.__place} for {self.__number_of_nights} nights\n")
    
    def cancel(self):
        print(f"Hotel booked in {self.__place} for {self.__number_of_nights} is cancelled\n")
    
    def generate_bill(self):
        total_amount = self.__number_of_nights * self.__rate_per_night
        print(f"Bill generated for Hotel Booking Service:\nCity: {self.__place}\nNumber of Nights: {self.__number_of_nights}\nBill Amount: Rs. {total_amount}\n")
        return total_amount