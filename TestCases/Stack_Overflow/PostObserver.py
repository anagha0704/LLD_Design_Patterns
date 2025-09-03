from abc import ABC, abstractmethod

class PostObserver(ABC):

    from Event import Event
    @abstractmethod
    def on_post_event(self, event: Event):
        pass