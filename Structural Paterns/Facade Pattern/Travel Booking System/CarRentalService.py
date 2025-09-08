from BookingService import BookingService

class CarRentalService(BookingService):
    def set_details(self, booking_config):
        self.__number_of_days = booking_config["number_of_days"]
        self.__rate_per_hour = 2000
        
    def book(self):
        print(f"Car booked for {self.__number_of_days} days\n")
    
    def cancel(self):
        print(f"Car booked for {self.__number_of_days} days is cancelled\n")
    
    def generate_bill(self):
        total_amount = self.__rate_per_hour * self.__number_of_days
        print(f"Bill generated for Car Rental Service:\nNumber of Days: {self.__number_of_days}\nBill Amount: Rs. {total_amount}\n")
        return total_amount