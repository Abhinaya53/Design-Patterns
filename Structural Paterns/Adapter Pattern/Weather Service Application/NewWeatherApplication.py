class NewWeatherApplication():
    def __init__(self, temperature, condition):
        self.__temperature = temperature
        self.__condition = condition

    def fetch_weather(self):
        return "weather: {\n\ttemperature: " + str(self.__temperature) + ",\n\tcondition: \"" + self.__condition + "\"\n}\n"