from DocumentFactoryInterface import DocumentFactoryInterface
from HTMLDocument import HTMLDocument

class HTMLDocumentFactory(DocumentFactoryInterface):
    def create_document(self) -> HTMLDocument:
        return HTMLDocument()