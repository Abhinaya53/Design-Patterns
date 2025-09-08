from ReportTemplate import ReportTemplate

class EmployeeReport(ReportTemplate):
    def _gather_data(self):
        print("\nGathering Employee Data")

    def _process_data(self):
        print("Processing Employee Data")