from UIFactory import UIFactory
from UIComponents import MacButton, MacCheckbox

class MacFactory(UIFactory):
    def create_button(self) -> MacButton:
        return MacButton()

    def create_checkbox(self) -> MacCheckbox:
        return MacCheckbox()