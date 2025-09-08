from Device import Device
from WeatherStation import WeatherStation

station = WeatherStation(Device())
station.set_temperature(30)
station.set_temperature(28)