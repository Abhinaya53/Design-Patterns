from TravelBookingSystem import TravelBookingSystem

booking_congig = {"source": "Chennai",
                  "destination": "Bangalore",
                  "number_of_nights": 3,
                  "number_of_days": 4}

travel_booking_system = TravelBookingSystem()
travel_booking_system.book_full_travel_package(booking_congig)
travel_booking_system.process_full_payment()
travel_booking_system.cancel_full_travel_package()