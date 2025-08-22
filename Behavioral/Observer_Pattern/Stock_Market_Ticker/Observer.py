from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, stock)->None:
        pass

    @abstractmethod
    def reaction(self):
        pass