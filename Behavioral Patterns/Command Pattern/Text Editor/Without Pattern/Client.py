from TextEditor import TextEditor
from BoldButton import BoldButton
from ItalicButton import ItalicButton

editor = TextEditor()
bold_button = BoldButton(editor)
italic_button = ItalicButton(editor)

bold_button.click()
italic_button.click()