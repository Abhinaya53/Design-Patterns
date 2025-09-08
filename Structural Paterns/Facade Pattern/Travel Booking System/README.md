# Problem:
You are designing a Travel Booking System that integrates with multiple subsystems:
- **FlightService:** Handles flight availability, booking, and cancellations.
- **HotelService:** Manages hotel rooms, reservations, and payments.
- **CarRentalService:** Provides rental car booking and return.
- **PaymentService:** Processes different modes of payment.

Currently, a client who wants to book a full travel package (flight + hotel + car + payment) must interact with all these services individually and handle complex coordination logic.

Design a solution that provides a single entry point for clients to:
- Book a complete trip (flight, hotel, and car rental).
- Cancel a complete trip in one call.
- Make a single payment that is distributed to respective services.