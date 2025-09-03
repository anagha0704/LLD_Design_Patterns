from States import States

class Playing(States):

    def play_track(self, player: "MediaPlayer")->None:
        print(f"Playing: Already Playing!!")

    def pause_track(self, player: "MediaPlayer")->None:
        print("Playing: Track Paused!!")
        from ConcreteStates.Paused import Paused
        player.set_state(Paused())

    def stop_track(self, player: "MediaPlayer")->None:
        print("Playing: Track Stopped!!")
        from ConcreteStates.Stopped import Stopped
        player.set_state(Stopped())