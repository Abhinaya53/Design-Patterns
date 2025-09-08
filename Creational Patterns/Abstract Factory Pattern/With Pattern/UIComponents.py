from ButtonInterface import ButtonInterface
from CheckboxInterface import CheckboxInterface

class WindowsButton(ButtonInterface):
    def render(self) -> None:
        print("Rendering Windows Button")

class MacButton(ButtonInterface):
    def render(self) -> None:
        print("Rendering Mac Button")

class WindowsCheckbox(CheckboxInterface):
    def render(self) -> None:
        print("Rendering Windows Checkbox")

class MacCheckbox(CheckboxInterface):
    def render(self) -> None:
        print("Rendering Mac Checkbox")