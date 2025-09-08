from Button import Button
from collections import defaultdict

class RemoteControlSystem:
    def __init__(self):
        self.__buttons = defaultdict(Button)
    
    def add_button(self, button_name, button: Button):
        self.__buttons[button_name] = button
    
    def button_click(self, button_name):
        self.__buttons[button_name].click()