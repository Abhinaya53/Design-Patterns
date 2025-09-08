from CommandInterface import CommandInterface

class Button:
    def __init__(self, command: CommandInterface):
        self.__command = command

    def click(self):
        self.__command.execute()