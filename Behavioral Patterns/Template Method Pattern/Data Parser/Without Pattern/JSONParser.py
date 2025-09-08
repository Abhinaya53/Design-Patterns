class JSONParser:
    def parse(self):
        self.__open_file()
        # JSON Specific Parsing Logic
        print("Parsing a JSON File")
        self.__close_file()

    def __open_file(self):
        print("\nOpening File")

    def __close_file(self):
        print("Closing File\n")