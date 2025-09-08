from DocumentFactoryInterface import DocumentFactoryInterface
from PDFDocument import PDFDocument

class PDFDocumentFactory(DocumentFactoryInterface):
    def create_document(self) -> PDFDocument:
        return PDFDocument()