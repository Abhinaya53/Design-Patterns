from FormatterStrategyInterface import FormatterStrategyInterface

class HTMLFormatter(FormatterStrategyInterface):
    def format(self, text: str) -> None:
        print(f"\nHTML Format:\n<html>\n\t<body>\n\t\t{text}\n\t</body>\n<html>\n")