from UIComponents import WindowsButton, MacButton, WindowsCheckbox, MacCheckbox

def create_gui(os_type):
    if os_type == "Windows":
        button = WindowsButton()
        checkbox = WindowsCheckbox()
        button.render()
        checkbox.render()
    elif os_type == "Mac":
        button = MacButton()
        checkbox = MacCheckbox()
        button.render()
        checkbox.render()
    else:
        raise ValueError("Unsupported OS type")

create_gui("Windows")
create_gui("Mac")