from StateInterface import StateInterface

class PlayingState(StateInterface):
    def __str__(self):
        return "Playing"
    
    def press_play(self):
        print("\nThe track is already playing...")
        return PlayingState()
    
    def press_pause(self):
        print("\nThe track is paused...")
        from PausedState import PausedState
        return PausedState()
    
    def press_stop(self):
        print("\nThe track is stopped...")
        from StoppedState import StoppedState
        return StoppedState()