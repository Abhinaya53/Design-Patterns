class Fan():
    def __init__(self):
        self.__state = "Off"
    
    def get_state(self):
        return self.__state
    
    def turn_on(self):
        self.__state = "On"
        print("Fan is Turned On")
    
    def turn_off(self):
        self.__state = "Off"
        print("Fan is Turned Off")