from StateInterface import StateInterface

class StoppedState(StateInterface):
    def __str__(self):
        return "Stopped"
    
    def press_play(self):
        print("\nThe track is playing...")
        from PlayingState import PlayingState
        return PlayingState()
    
    def press_pause(self):
        print("\nThe track is paused...")
        from PausedState import PausedState
        return PausedState()
    
    def press_stop(self):
        print("\nThe track is already stopped...")
        return StoppedState()

