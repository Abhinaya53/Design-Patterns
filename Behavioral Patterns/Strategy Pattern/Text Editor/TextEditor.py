from FormatterStrategyInterface import FormatterStrategyInterface

class TextEditor:               # Context
    def __init__(self):
        self.__format_style = None

    def set_format_style(self, format_style) -> None:
        self.__format_style: FormatterStrategyInterface = format_style
    
    def display(self, text: str) -> None:
        if not self.__format_style:
            print("Please set a format style first.")
        else:
            self.__format_style.format(text)