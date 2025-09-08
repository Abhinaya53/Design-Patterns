from Mediator import Mediator
from Flight import Flight
from collections import deque

class FlightControlTower(Mediator):
    def __init__(self):
        self.__takeoff_runway = 2
        self.__landing_runway = 2
        self.__waiting_takeoff = deque()
        self.__waiting_landing = deque()
        self.__flights = set()
        
    def register_flight(self, flight):
        if flight in self.__flights:
            print(f"Warning: Flight {flight.get_id()} is already registered.")
        else:
            self.__flights.add(flight)

    def handle_takeoff_request(self, flight: Flight):
        if self.__takeoff_runway < 1:
            print("Take-Off permission denied: Runway not available")
            self.__waiting_takeoff.append(flight)
            return "Waiting Take-Off"
        else:
            print(f"Take-Off cleared: Use Runway {self.__takeoff_runway}")
            self.__takeoff_runway -= 1
            return "TakingOff"

    def handle_landing_request(self, flight: Flight):
        if self.__landing_runway < 1:
            print("Landing permission denied: Runway not available")
            self.__waiting_landing.append(flight)
            return "Waiting Landing"
        else:
            print(f"Landing cleared: Use Runway {self.__landing_runway}")
            self.__landing_runway -= 1
            return "Landing"
        
    def notify_takeoff_complete(self, flight: Flight):
        self.__takeoff_runway += 1
        if self.__waiting_takeoff and self.__takeoff_runway > 0:
            next_flight = self.__waiting_takeoff.popleft()
            status = self.handle_takeoff_request(next_flight)
            if status == "TakingOff":
                print(f"Aircraft {next_flight.get_id()} Take-Off: SUCCESS")
                next_flight.complete_takeoff()

    def notify_landing_complete(self, flight: Flight):
        self.__landing_runway += 1
        if self.__waiting_landing and self.__landing_runway > 0:
            next_flight = self.__waiting_landing.popleft()
            status = self.handle_landing_request(next_flight)
            if status == "Landing":
                print(f"Aircraft {next_flight.get_id()} Landing: SUCCESS")
                next_flight.complete_landing()