from DocumentEditor import DocumentEditor

editor = DocumentEditor()
editor.add_character("A", "Ariel", 13, "red")
editor.add_character("B", "Calibri", 12, "blue")
editor.add_character("H", "Ariel", 12, "blue")
editor.add_character("I", "Ariel", 13, "red")

editor.render()