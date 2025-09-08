class Document:
    def __init__(self):
        self.__content: str = ""
        self.__state = "Draft"      # Default State
    
    def write_content(self, content: str):
        if self.__state == "Published":
            print("\nCan't edit content after publishing!")
        else:
            self.__content = content
    
    def get_content(self):
        return self.__content

    def publish(self):
        match self.__state:
            case "Draft":
                print(f"\nPublishing {self.__state} Document...")
                self.__state = "Moderation"
                print(f"Current State of Document: {self.__state}")
                print(f"Content:\n{self.__content}")
            case "Moderation":
                print(f"\nPublishing {self.__state} Document...")
                self.__state = "Published"
                print(f"Current State of Document: {self.__state}")
                print(f"Content:\n{self.__content}")
            case "Published":
                print(f"\nDocument is already in {self.__state} state...")
                print(f"Content:\n{self.__content}")