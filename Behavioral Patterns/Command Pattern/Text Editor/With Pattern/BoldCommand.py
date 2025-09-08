from TextEditor import TextEditor
from CommandInterface import CommandInterface

class BoldCommand(CommandInterface):
    def __init__(self, editor: TextEditor) -> None:
        self.__editor = editor

    def execute(self) -> None:
        self.__editor.bold_text()