from DocumentInterface import DocumentInterface

class PDFDocument(DocumentInterface):
    def open(self):
        return "Opening PDF Document"
    
    def save(self):
        return "Saving PDF Document"
    
    def close(self):
        return "Closing PDF Document"