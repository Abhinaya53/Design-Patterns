from WeatherApplication import WeatherApplication
from LegacyWeatherApplication import LegacyWeatherApplication
from NewWeatherApplication import NewWeatherApplication
from NewWeatherApplicationAdapter import NewWeatherApplicationAdapter

def print_weather_data(app: WeatherApplication):
    print(app.get_weather_data())

app1 = LegacyWeatherApplication(26, "Cloudy")
print_weather_data(app1)

app2 = NewWeatherApplicationAdapter(NewWeatherApplication(24, "Rainy"))
print_weather_data(app2)