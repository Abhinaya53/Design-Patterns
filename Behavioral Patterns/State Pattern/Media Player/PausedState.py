from StateInterface import StateInterface

class PausedState(StateInterface):
    def __str__(self):
        return "Paused"
    
    def press_play(self):
        print("\nThe track is playing...")
        from PlayingState import PlayingState
        return PlayingState()
    
    def press_pause(self):
        print("\nThe track is already paused...")
        return PausedState()
    
    def press_stop(self):
        print("\nThe track is stopped...")
        from StoppedState import StoppedState
        return StoppedState()