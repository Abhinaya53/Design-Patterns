from FormatterStrategyInterface import FormatterStrategyInterface

class PlainTextFormatter(FormatterStrategyInterface):
    def format(self, text: str) -> None:
        print(f"\nPlain Text Format:\n{text}\n")