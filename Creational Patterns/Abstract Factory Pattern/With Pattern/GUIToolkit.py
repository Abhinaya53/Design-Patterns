from UIFactory import UIFactory
from WindowsFactory import WindowsFactory
from MacFactory import MacFactory

def create_gui(factory: UIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.render()
    checkbox.render()
    

create_gui(WindowsFactory())
create_gui(MacFactory())