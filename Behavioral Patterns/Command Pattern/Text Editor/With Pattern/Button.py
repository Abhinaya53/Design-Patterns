from TextEditor import TextEditor
from CommandInterface import CommandInterface

class Button:
    def __init__(self, command: CommandInterface):
        self.__command = command
    
    def click(self) -> None:
        self.__command.execute()