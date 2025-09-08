from DataSource import DataSource

class FileDataSource(DataSource):
    def __init__(self) -> None:
        self._data = ""

    def read_file(self) -> str:
        return self._data
    
    def write_file(self, data: str) -> None:
        self._data = data