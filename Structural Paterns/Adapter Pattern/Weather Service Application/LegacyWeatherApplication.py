from WeatherApplication import WeatherApplication

class LegacyWeatherApplication(WeatherApplication):
    def __init__(self, temperature, condition):
        self.__temperature = temperature
        self.__condition = condition

    def get_weather_data(self):
        return f"<weather>\n\t<temperature> {self.__temperature} </temperature>\n\t<condition> {self.__condition} </condition>\n</weather>\n"