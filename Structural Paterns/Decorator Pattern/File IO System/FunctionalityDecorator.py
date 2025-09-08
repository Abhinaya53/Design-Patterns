from DataSource import DataSource

class FunctionalityDecorator(DataSource):
    def __init__(self, data_source: DataSource):
        self._data_source = data_source
    
    def read_file(self) -> str:
        return self._data_source.read_file()
    
    def write_file(self, data: str) -> None:
        self._data_source.write_file(data)