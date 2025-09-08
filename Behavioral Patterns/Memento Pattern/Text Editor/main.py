from Editor import Editor
from Snapshot import Snapshot
from HistoryManager import HistoryManager

editor = Editor()
history_manager = HistoryManager()

editor.write("Hello. This is Abhinaya!")
history_manager.save(editor)
print(editor.get_content())

editor.write("Hi! I am Abhinaya..")
history_manager.save(editor)
print(editor.get_content())

history_manager.undo(editor)
print(editor.get_content())