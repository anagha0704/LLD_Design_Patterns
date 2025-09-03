from States import States

class Paused(States):

    def play_track(self, player: "MediaPlayer")->None:
        print(f"Paused: Playback resumed!!")
        from ConcreteStates.Playing import Playing
        player.set_state(Playing())

    def pause_track(self, player: "MediaPlayer")->None:
        print("Paused: Already Paused!!")

    def stop_track(self, player: "MediaPlayer")->None:
        print("Paused: Track Stopped!!")
        from ConcreteStates.Stopped import Stopped
        player.set_state(Stopped())