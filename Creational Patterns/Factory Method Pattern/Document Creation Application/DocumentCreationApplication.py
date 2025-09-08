from DocumentFactoryInterface import DocumentFactoryInterface
from PDFDocumentFactory import PDFDocumentFactory
from WordDocumentFactory import WordDocumentFactory
from HTMLDocumentFactory import HTMLDocumentFactory

def manage_document(factory: DocumentFactoryInterface):
    document = factory.create_document()
    print(document.open())
    print(document.save())
    print(document.close())