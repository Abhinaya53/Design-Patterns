from MobileDevice import MobileDevice
from TabletDevice import TabletDevice
from WeatherStation import WeatherStation

station = WeatherStation()

mobile1 = MobileDevice("Abhi Mobile")
station.subscribe(mobile1)

mobile2 = MobileDevice("Akshay Mobile")
station.subscribe(mobile2)

tablet1 = TabletDevice("Abhi Tablet")
station.subscribe(tablet1)

tablet2 = TabletDevice("Akshay Tablet")
station.subscribe(tablet2)

print()
station.set_temperature(30)
print()
station.set_temperature(28)
print()
station.unsubscribe(tablet2)
station.set_temperature(23)
print()