"""
Originator Class: Editor

"""

from Snapshot import Snapshot

class Editor:
    def __init__(self) -> None:
        self.__content = ""
    
    def write(self, content: str) -> None:
        self.__content = content
    
    def save_state(self) -> Snapshot:
        return Snapshot(self.__content)
    
    def restore_state(self, snapshot: Snapshot) -> None:
        self.__content = snapshot.get_content()
    
    def get_content(self) -> str:
        return self.__content