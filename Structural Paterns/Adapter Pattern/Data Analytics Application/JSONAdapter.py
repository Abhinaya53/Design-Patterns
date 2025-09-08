from DataProvider import DataProvider
from JSONDataProvider import JSONDataProvider

class JSONAdapter(DataProvider):
    def __init__(self, json_provider: JSONDataProvider):
        self.__json_provider = json_provider

    def get_results(self):
        self.__json_provider.generate_results()