from StateInterface import StateInterface
from DraftState import DraftState

class Document:         # Context Class
    def __init__(self):
        self.__content: str = ""
        self.__state = DraftState()      # Default State: Draft
    
    def write_content(self, content: str):
        if self.__state.can_write():
            self.__content = content
     
    def get_content(self):
        return self.__content

    def publish(self):
        self.__state = self.__state.publish_process()
        print(f"Current State of Document: {self.__state}")
        print(f"Content:\n{self.__content}")