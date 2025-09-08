class CSVParser:
    def parse(self):
        self.__open_file()
        # CSV Specific Parsing Logic
        print("Parsing a CSV File")
        self.__close_file()

    def __open_file(self):
        print("\nOpening File")

    def __close_file(self):
        print("Closing File\n")