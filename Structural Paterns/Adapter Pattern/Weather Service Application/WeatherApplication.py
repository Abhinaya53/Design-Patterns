from abc import ABC, abstractmethod

class WeatherApplication(ABC):
    @abstractmethod
    def get_weather_data(self):
        pass