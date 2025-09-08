from StateInterface import StateInterface

class PublishedState(StateInterface):
    def __str__(self):
        return "Published"
    
    def can_write(self):
        print("\nCan't edit content after publishing!")
        return False
    
    def publish_process(self):
        print(f"\nDocument is already in Published state...")
        return PublishedState()