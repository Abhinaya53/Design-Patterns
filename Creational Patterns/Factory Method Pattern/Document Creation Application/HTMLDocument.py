from DocumentInterface import DocumentInterface

class HTMLDocument(DocumentInterface):
    def open(self):
        return "Opening HTML Document"
    
    def save(self):
        return "Saving HTML Document"
    
    def close(self):
        return "Closing HTML Document"