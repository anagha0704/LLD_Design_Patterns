from ConcreteStates.Stopped import Stopped

class MediaPlayer:

    def __init__(self):
        self.state = Stopped()
    
    def set_state(self, state)->None:
        self.state = state

    def play(self)->None:
        self.state.play_track(self)

    def pause(self)->None:
        self.state.pause_track(self)

    def stop(self)->None:
        self.state.stop_track(self)