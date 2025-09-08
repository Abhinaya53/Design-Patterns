from GraphicEditor import GraphicEditor

class Caretaker:
    def __init__(self):
        self.__history = []
    
    def save(self, editor: GraphicEditor) -> None:
        self.__history.append(editor.save_state())
    
    def undo(self, editor: GraphicEditor) -> None:
        if self.__history:
            self.__history.pop()
            editor.restore_state(self.__history[-1])