from StateInterface import StateInterface
from PublishedState import PublishedState

class ModerationState(StateInterface):
    def __str__(self):
        return "Moderation"
    
    def can_write(self):
        return True
    
    def publish_process(self):
        print(f"\nPublishing Moderation Document...")
        return PublishedState()