from TextEditor import TextEditor
from MarkdownFormatter import MarkdownFormatter
from PlainTextFormatter import PlainTextFormatter
from HTMLFormatter import HTMLFormatter

service = TextEditor()

text = "Hi! This is Abhinaya."

service.set_format_style(PlainTextFormatter())
service.display(text)

service.set_format_style(HTMLFormatter())
service.display(text)

service.set_format_style(MarkdownFormatter())
service.display(text) 