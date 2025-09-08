from FunctionalityDecorator import FunctionalityDecorator

class BufferingDecorator(FunctionalityDecorator):
    def __init__(self, data_source):
        super().__init__(data_source)

    def read_file(self) -> None:
        return super().read_file()
    
    def write_file(self, data):
        super().write_file(f"<buffer>{data}</buffer>")