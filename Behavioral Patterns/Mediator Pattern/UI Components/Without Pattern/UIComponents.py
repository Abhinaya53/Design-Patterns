class Button:
    def enable(self):
        print("Button enabled") 

    def disable(self):
        print("Button disabled")

class TextField:    
    def enable(self):
        print("TextField enabled") 
        
    def disable(self):
        print("TextField disabled")

class Checkbox:
    def __init__(self, text_field, button):
        self.text_field = text_field
        self.button = button

    def check(self):
        print("\nCheckbox checked")
        self.text_field.enable()
        self.button.enable()

    def uncheck(self):
        print("\nCheckbox checked")
        self.text_field.disable()
        self.button.disable()