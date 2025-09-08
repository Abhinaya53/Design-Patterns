from StateInterface import StateInterface
from ModerationState import ModerationState

class DraftState(StateInterface):
    def __str__(self):
        return "Draft"
    
    def can_write(self):
        return True

    def publish_process(self):
        print(f"\nPublishing Draft Document...")
        return ModerationState()