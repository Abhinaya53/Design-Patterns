from NetworkService import NetworkService
from RealNetworkService import RealNetworkService

class NetworkServiceProxy(NetworkService):
    def __init__(self):
        self.__real_network_service = None
        self.__cache = {}
    
    def fetch_data(self, key):
        if key in self.__cache:
            print("Fetching from Cache...")
            return self.__cache[key]
        
        if not self.__real_network_service:
            self.__real_network_service = RealNetworkService()

        self.__cache[key] = self.__real_network_service.fetch_data(key)
        return self.__cache[key]