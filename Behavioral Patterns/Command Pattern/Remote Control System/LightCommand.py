from Light import Light 
from CommandInterface import CommandInterface

class LightCommand(CommandInterface):
    def __init__(self, light: Light):
        self.__light  = light

    def execute(self):
        if self.__light.get_state() == "On":
            self.__light.turn_off()
        else:
            self.__light.turn_on()