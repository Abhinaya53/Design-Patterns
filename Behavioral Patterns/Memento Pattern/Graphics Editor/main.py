from Caretaker import Caretaker
from GraphicEditor import GraphicEditor

caretaker = Caretaker()
graphic_editor = GraphicEditor()

graphic_editor.set_shape("square", 4, 2, "red", 16)
caretaker.save(graphic_editor)
print(graphic_editor.get_shape_type())

graphic_editor.set_shape("circle", 2, 5, "blue", 50)
caretaker.save(graphic_editor)
print(graphic_editor.get_shape_type())

caretaker.undo(graphic_editor)
print(graphic_editor.get_shape_type())