from DocumentFactoryInterface import DocumentFactoryInterface
from WordDocument import WordDocument

class WordDocumentFactory(DocumentFactoryInterface):
    def create_document(self) -> WordDocument:
        return WordDocument()