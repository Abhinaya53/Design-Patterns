from DocumentInterface import DocumentInterface

class WordDocument(DocumentInterface):
    def open(self):
        return "Opening Word Document"
    
    def save(self):
        return "Saving Word Document"
    
    def close(self):
        return "Closing Word Document"