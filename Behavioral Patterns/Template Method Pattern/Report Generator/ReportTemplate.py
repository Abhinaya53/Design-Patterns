from abc import ABC, abstractmethod

class ReportTemplate(ABC):
    def generate_report(self):          # Method not to be overidden in any base class
        self._gather_data()
        self._process_data()
        self._format_data()
        self._print_data()

    @abstractmethod
    def _gather_data(self):
        pass

    @abstractmethod
    def _process_data(self):
        pass

    def _format_data(self):
        print("Formatting Processed Data")

    def _print_data(self):
        print("Printing Printing Data\n")