from Button import Button
from Checkbox import Checkbox
from Dialog import Dialog
from TextField import TextField

dialog = Dialog()
dialog.add_component(Button())
dialog.add_component(TextField())

checkbox = Checkbox(dialog)
checkbox.check()
checkbox.uncheck()