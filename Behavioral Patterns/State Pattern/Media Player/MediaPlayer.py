from StateInterface import StateInterface
from StoppedState import StoppedState

class MediaPlayer:
    def __init__(self):
        self.__state: StateInterface = StoppedState()           # Initial State
    
    def play(self):
        self.__state = self.__state.press_play()
        print(f"Current State: {self.__state}")

    def pause(self):
        self.__state = self.__state.press_pause()
        print(f"Current State: {self.__state}")
    
    def stop(self):
        self.__state = self.__state.press_stop()
        print(f"Current State: {self.__state}")