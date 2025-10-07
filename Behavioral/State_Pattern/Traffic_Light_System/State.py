from abc import ABC, abstractmethod

class State(ABC):

    @abstractmethod
    def display(self)->None:
        pass

    @abstractmethod
    def change(self)->"State":
        pass