from Fan import Fan 
from CommandInterface import CommandInterface

class FanCommand(CommandInterface):
    def __init__(self, fan: Fan):
        self.__fan  = fan

    def execute(self):
        if self.__fan.get_state() == "On":
            self.__fan.turn_off()
        else:
            self.__fan.turn_on()