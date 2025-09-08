from Flight import Flight
from FlightControlTower import FlightControlTower

tower = FlightControlTower()

flight1 = Flight("AI-202", tower)
flight2 = Flight("AI-303", tower)
flight3 = Flight("AI-404", tower)
flight4 = Flight("AI-505", tower)

tower.register_flight(flight1)
tower.register_flight(flight2)
tower.register_flight(flight3)
tower.register_flight(flight4)

flight1.request_takeoff()
flight2.request_takeoff()
flight3.request_takeoff()

flight1.request_landing()
flight2.request_landing()
flight3.request_landing()

flight4.request_landing()
flight4.request_takeoff()