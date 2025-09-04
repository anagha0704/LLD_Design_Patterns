from abc import ABC, abstractmethod

class IntersectionState(ABC):

    @abstractmethod
    def handle(self, context: "IntersectionController")->None:
        pass