from States import States

class Stopped(States):

    def play_track(self, player: "MediaPlayer")->None:
        print(f"Stopped: Playback started!!")
        from ConcreteStates.Playing import Playing
        player.set_state(Playing())

    def pause_track(self, player: "MediaPlayer")->None:
        print("Stopped: In Stopped state. Nothig to pause")

    def stop_track(self, player: "MediaPlayer")->None:
        print("Stopped: Nothing playing to stop!!")