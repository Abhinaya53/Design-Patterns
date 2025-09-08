"""
Memento Class : Snapshot
"""

class Snapshot:
    def __init__(self, content: str) -> None:
        self.__content = content
    
    def get_content(self) -> str:
        return self.__content