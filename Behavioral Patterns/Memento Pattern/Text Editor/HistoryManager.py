"""
Caretaker Class: HistoryManager
"""

from Snapshot import Snapshot
from Editor import Editor

class HistoryManager:
    def __init__(self) -> None:
        self.__stack = []
    
    def save(self, editor: Editor) -> None:
        self.__stack.append(editor.save_state())
    
    def undo(self, editor: Editor) -> None:
        if self.__stack:
            self.__stack.pop()
            editor.restore_state(self.__stack[-1])