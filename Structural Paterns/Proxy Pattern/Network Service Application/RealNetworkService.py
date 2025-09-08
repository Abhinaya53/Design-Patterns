from NetworkService import NetworkService

class RealNetworkService(NetworkService):
    def fetch_data(self, key):
        return f"Fetching data from remote server with key {key}\n"