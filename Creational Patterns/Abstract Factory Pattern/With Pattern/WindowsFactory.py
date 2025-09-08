from UIFactory import UIFactory
from UIComponents import WindowsButton, WindowsCheckbox

class WindowsFactory(UIFactory):
    def create_button(self) -> WindowsButton:
        return WindowsButton()

    def create_checkbox(self) -> WindowsCheckbox:
        return WindowsCheckbox()