from WeatherApplication import WeatherApplication
from NewWeatherApplication import NewWeatherApplication

class NewWeatherApplicationAdapter(WeatherApplication):
    def __init__(self, new_weather_application: NewWeatherApplication):
        self.__new_weather_application = new_weather_application

    def get_weather_data(self):
        return self.__new_weather_application.fetch_weather()