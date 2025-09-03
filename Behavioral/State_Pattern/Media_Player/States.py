from abc import ABC, abstractmethod

class States(ABC):

    @abstractmethod
    def play_track(self, player: "MediaPlayer")->None:
        pass

    @abstractmethod
    def pause_track(self, player: "MediaPlayer")->None:
        pass

    @abstractmethod
    def stop_track(self, player: "MediaPlayer")->None:
        pass