from TextEditor import TextEditor

class ItalicButton:
    def __init__(self, editor: TextEditor):
        self.editor = editor

    def click(self):
        self.editor.italicize_text()