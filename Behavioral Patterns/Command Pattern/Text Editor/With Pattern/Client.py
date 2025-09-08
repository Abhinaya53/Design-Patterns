from TextEditor import TextEditor
from BoldCommand import BoldCommand
from ItalicCommand import ItalicCommand
from UnderlineCommand import UnderlineCommand
from Button import Button

editor = TextEditor()

button1 = Button(BoldCommand(editor))
button1.click()

button2 = Button(ItalicCommand(editor))
button2.click()

button3 = Button(UnderlineCommand(editor))
button3.click()