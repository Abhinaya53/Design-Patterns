from TextEditor import TextEditor

class BoldButton:
    def __init__(self, editor: TextEditor) -> None:
        self.editor = editor

    def click(self) -> None:
        self.editor.bold_text()