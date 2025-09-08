from HideableUIComponent import HideableUIComponent

class Button(HideableUIComponent):
    def enable(self):
        print("Button enabled") 

    def disable(self):
        print("Button disabled")