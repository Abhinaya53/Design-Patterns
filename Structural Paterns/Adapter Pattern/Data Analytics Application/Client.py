from DataProvider import DataProvider
from CSVDataProvider import CSVDataProvider
from JSONDataProvider import JSONDataProvider
from JSONAdapter import JSONAdapter

def print_results(provider: DataProvider):
    provider.get_results()

provider1 = CSVDataProvider()
print_results(provider1)

provider2 = JSONAdapter(JSONDataProvider())
print_results(provider2)