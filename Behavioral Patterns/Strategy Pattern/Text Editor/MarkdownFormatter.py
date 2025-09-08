from FormatterStrategyInterface import FormatterStrategyInterface

class MarkdownFormatter(FormatterStrategyInterface):
    def format(self, text: str) -> None:
        print(f"\nMarkdown Format:\n**{text}**\n")