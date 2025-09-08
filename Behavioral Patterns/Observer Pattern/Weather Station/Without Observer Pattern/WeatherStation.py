from Device import Device

class WeatherStation:
    def __init__(self, device: Device) -> None:
        self.__device = device

    def set_temperature(self, temp: float) -> None:
        self.__temperature = temp
        self.notify_device()
    
    def get_temperature(self) -> float:
        return self.__temperature
    
    def notify_device(self):
        self.__device.showTemperature(self.__temperature)