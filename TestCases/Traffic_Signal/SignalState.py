from abc import ABC, abstractmethod

class SignalState(ABC):

    @abstractmethod
    def handle(self, context: 'TrafficLight')->None:
        pass
    